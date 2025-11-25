#!/usr/bin/env python3
from string import ascii_letters
from random import SystemRandom
from asyncio import sleep
from telegraph.aio import Telegraph
from telegraph.exceptions import RetryAfterError

from bot import LOGGER, bot_loop, config_dict


class TelegraphHelper:
    def __init__(self, author_name=None, author_url=None):
        self.telegraph = Telegraph(domain='graph.org')
        self.short_name = ''.join(SystemRandom().choices(ascii_letters, k=8))
        self.access_token = None
        self.author_name = author_name
        self.author_url = author_url

    async def create_account(self):
        await self.telegraph.create_account(
            short_name=self.short_name,
            author_name=self.author_name,
            author_url=self.author_url
        )
        self.access_token = self.telegraph.get_access_token()
        LOGGER.info(f"📝 Telegraph Account Generated : {self.short_name}")

    async def create_page(self, title, content):
        try:
            return await self.telegraph.create_page(
                title=title,
                author_name=self.author_name,
                author_url=self.author_url,
                html_content=content
            )
        except RetryAfterError as st:
            LOGGER.warning(
                f"⚠️ Telegraph Flood control exceeded. Sleeping for {st.retry_after} seconds."
            )
            await sleep(st.retry_after)
            return await self.create_page(title, content)

    async def edit_page(self, path, title, content):
        try:
            return await self.telegraph.edit_page(
                path=path,
                title=title,
                author_name=self.author_name,
                author_url=self.author_url,
                html_content=content
            )
        except RetryAfterError as st:
            LOGGER.warning(
                f"⚠️ Telegraph Flood control exceeded. Sleeping for {st.retry_after} seconds."
            )
            await sleep(st.retry_after)
            return await self.edit_page(path, title, content)

    async def edit_telegraph(self, path, telegraph_content):
        nxt_page = 1
        prev_page = 0
        num_of_path = len(path)
        
        for content in telegraph_content:
            # Navigation buttons styling
            nav_buttons = []
            
            if nxt_page == 1:
                nav_buttons.append(
                    f'<a href="https://telegra.ph/{path[nxt_page]}">Next ➡️</a>'
                )
                nxt_page += 1
            else:
                if prev_page <= num_of_path:
                    nav_buttons.append(
                        f'<a href="https://telegra.ph/{path[prev_page]}">⬅️ Prev</a>'
                    )
                    prev_page += 1
                if nxt_page < num_of_path:
                    nav_buttons.append(
                        f'<a href="https://telegra.ph/{path[nxt_page]}">Next ➡️</a>'
                    )
                    nxt_page += 1
            
            # Add navigation bar
            if nav_buttons:
                nav_bar = f'''
                <br><br>
                <p style="text-align: center;">
                    <b>{'  |  '.join(nav_buttons)}</b>
                </p>
                '''
                content += nav_bar
            
            await self.edit_page(
                path=path[prev_page],
                title=f"🔍 {config_dict['TITLE_NAME']} Torrent Search",
                content=content
            )
        return

    @staticmethod
    def format_search_result(results):
        """Format search results with modern styling"""
        formatted = '<br>'
        
        for idx, result in enumerate(results, 1):
            formatted += f'''
            <p>
                <b>{idx}. 📁 {result.get('name', 'Unknown')}</b><br>
                ├ 📦 Size: <code>{result.get('size', 'N/A')}</code><br>
                ├ 🌱 Seeds: <code>{result.get('seeds', '0')}</code><br>
                ├ 🔻 Leeches: <code>{result.get('leeches', '0')}</code><br>
                └ 🔗 <a href="{result.get('link', '#')}">Download Link</a>
            </p>
            <br>
            '''
        
        return formatted

    @staticmethod
    def format_drive_result(results):
        """Format drive search results with modern styling"""
        formatted = '<br>'
        
        for idx, result in enumerate(results, 1):
            file_type = result.get('type', 'file')
            emoji = '📂' if file_type == 'folder' else '📄'
            
            formatted += f'''
            <p>
                <b>{idx}. {emoji} {result.get('name', 'Unknown')}</b><br>
                ├ 📦 Size: <code>{result.get('size', 'N/A')}</code><br>
                ├ 📍 Path: <code>{result.get('path', 'N/A')}</code><br>
                ├ 🔗 <a href="{result.get('drive_link', '#')}">Drive Link</a><br>
                └ 🌐 <a href="{result.get('index_link', '#')}">Index Link</a>
            </p>
            <br>
            '''
        
        return formatted

    @staticmethod
    def create_header(title, subtitle=None):
        """Create a styled header for Telegraph pages"""
        header = f'''
        <h3 style="text-align: center;">🔰 {title}</h3>
        '''
        
        if subtitle:
            header += f'''
            <p style="text-align: center;"><i>{subtitle}</i></p>
            '''
        
        header += '<hr><br>'
        return header

    @staticmethod
    def create_footer():
        """Create a styled footer for Telegraph pages"""
        return '''
        <br><hr>
        <p style="text-align: center;">
            <i>🤖 Powered by Mirror Bot</i>
        </p>
        '''


telegraph = TelegraphHelper(
    config_dict['AUTHOR_NAME'],
    config_dict['AUTHOR_URL']
)

bot_loop.run_until_complete(telegraph.create_account())
