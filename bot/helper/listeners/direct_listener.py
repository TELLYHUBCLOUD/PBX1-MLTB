#!/usr/bin/env python3
from time import sleep

from bot import LOGGER, aria2
from bot.helper.ext_utils.bot_utils import async_to_sync, sync_to_async


class DirectListener:
    def __init__(self, foldername, total_size, path, listener, a2c_opt):
        self.__path = path
        self.__listener = listener
        self.__is_cancelled = False
        self.__a2c_opt = a2c_opt
        self.__proc_bytes = 0
        self.__failed = 0
        self.task = None
        self.name = foldername
        self.total_size = total_size

    @property
    def processed_bytes(self):
        if self.task:
            return self.__proc_bytes + self.task.completed_length
        return self.__proc_bytes

    @property
    def speed(self):
        return self.task.download_speed if self.task else 0

    def download(self, contents):
        self.is_downloading = True
        
        for content in contents:
            if self.__is_cancelled:
                break
            
            # Set download directory
            if content['path']:
                self.__a2c_opt['dir'] = f"{self.__path}/{content['path']}"
            else:
                self.__a2c_opt['dir'] = self.__path
            
            filename = content['filename']
            self.__a2c_opt['out'] = filename
            
            # Add download to aria2
            try:
                self.task = aria2.add_uris(
                    [content['url']], 
                    self.__a2c_opt, 
                    position=0
                )
            except Exception as e:
                self.__failed += 1
                LOGGER.error(f'❌ Unable to download {filename} due to: {e}')
                continue
            
            self.task = self.task.live
            
            # Monitor download progress
            while True:
                if self.__is_cancelled:
                    if self.task:
                        self.task.remove(True, True)
                    break
                
                self.task = self.task.live
                
                if error_message := self.task.error_message:
                    self.__failed += 1
                    LOGGER.error(
                        f'❌ Unable to download {self.task.name} due to: {error_message}'
                    )
                    self.task.remove(True, True)
                    break
                
                elif self.task.is_complete:
                    self.__proc_bytes += self.task.total_length
                    self.task.remove(True)
                    break
                
                sleep(1)
            
            self.task = None
        
        # Handle completion
        if self.__is_cancelled:
            return
        
        if self.__failed == len(contents):
            async_to_sync(
                self.__listener.onDownloadError,
                '❌ <b>Download Failed!</b>\n\n'
                '📌 All files failed to download.'
            )
            return
        
        async_to_sync(self.__listener.onDownloadComplete)

    async def cancel_download(self):
        self.__is_cancelled = True
        LOGGER.info(f"🚫 Cancelling Download: {self.name}")
        
        await self.__listener.onDownloadError(
            "🚫 <b>Download Cancelled!</b>\n\n"
            "📌 Cancelled by user request."
        )
        
        if self.task:
            await sync_to_async(self.task.remove, force=True, files=True)
