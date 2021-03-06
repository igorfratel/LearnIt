#! /usr/bin/python3
import datetime
import time
from UserManager import UserManager
from UserSendingCardManager import UserSendingCardManager
from utilities import logging_utils
import logging
import gc
import threading


class SendingManager():

	def __init__(self, sleep, bot_controller_factory, debug_mode):
		self.__stop = threading.Event()

		self.sleep = sleep
		self.debug_mode = debug_mode
		self.bot_logger = logging.getLogger('Bot_Sender')
		self.logger = logging.getLogger('Sending_Manager')
		self.user_manager = UserManager(bot_controller_factory, self.debug_mode)
		self.users = self.user_manager.users
		self.user_card_manager = {}


	def upd_users(self):
		self.user_manager.update_users()
		self.users = self.user_manager.users
		for user_id, user in self.users.items():
			if user.get_active() == 0:
				continue
			if not (user_id in self.user_card_manager.keys()):
				self.user_card_manager[user_id] = UserSendingCardManager(user)

	def stop(self):
		self.__stop.set()

	def run(self):
		self.__stop.clear()

		cycles = 0
		while not self.__stop.wait(self.sleep):
			try:
				if cycles % 2 == 0:
					self.logger.warning("Collect garbage")
					gc.collect()

				self.logger.warning("SM Woke Up - Cycles: {}".format(cycles))
				cycles += 1
				self.upd_users()
				for user_id, user_card_manager in self.user_card_manager.items():
					if self.users[user_id].get_active() == 0:
						continue
					user_card_manager.run()
				self.logger.info("Sleep {}".format(self.sleep))
			except Exception as e:
				self.bot_logger.error("EXCEPTION on SM", exc_info=True)
				self.logger.error("EXCEPTION on SM", exc_info=True)

		self.logger.warning("SM turned off")
		self.bot_logger.warning("SM turned off")


class SendingManagerThread(threading.Thread):

	def __init__(self, sending_manager):
		threading.Thread.__init__(self, name="SendingManagerThread")
		self.sending_manager = sending_manager

	def stop(self):
		self.sending_manager.stop()

	def run(self):
		self.sending_manager.run()

if __name__ == '__main__':
	from BotController import BotControllerFactory
	sending_manager = SendingManager(5, BotControllerFactory('495750247:AAFVO7YqWCl2QKov6PselFnAlL_RRBtfWco'), 1)
	sending_manager_thread = SendingManagerThread(sending_manager)
	sending_manager_thread.start()
