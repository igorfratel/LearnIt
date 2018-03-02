import time
import logging
from utilities import logging_utils

def check_logger(user_id, logger, debug_mode):
	if (not user_id in logger.keys()):
		logger[user_id] = logging.getLogger(__name__)
		path = '../logs/user_ops{}.log'.format(user_id)
		if debug_mode:
			path = '../logs_debug/user_ops{}.log'.format(user_id)

		bot = bot_utils.open_bot(debug_mode, logger)
		logger[user_id] = logging_utils.setup_logger_default(logger[user_id], path, bot) 
	


class UserOps():

	def __init__(self, conn, cursor, debug_mode):
		self.debug_mode = debug_mode
		self.logger = {}
		self.conn = conn
		self.cursor = cursor

	def get_state(self, user_id):
		"""Gets the current state information about the user

		Args:
			user_id: An integer representing the user's id.

		Returns:
			A tuple containing two integers, the primary and secondary states of the user.
		"""
		tries = 5
		while tries > 0:
			tries -= 1
			cmd = "SELECT state1, state2, state3 FROM users WHERE id=%s"
			try:
				self.cursor.execute(cmd, (user_id, ))
				row = self.cursor.fetchall()
				if len(row) == 0:
					return "User doesn't exist"
				return (row[0][0], row[0][1], row[0][2])
			except:
				check_logger(user_id, self.logger, self.debug_mode)
				self.logger[user_id].error("Error get_state", exc_info=True)
				time.sleep(1)
		return []



	def set_state(self, user_id, state1, state2, state3):
		"""Updates on the database the state information about the user
			
		Args:
			user_id: An integer representing the user's id.
			state: An integer representing the user's primary state.
			state2: An integer representing the user's secondary state.
		"""
		tries = 5
		while tries > 0:
			tries -= 1
			cmd = "UPDATE users SET state1=%s, state2=%s, state3=%s WHERE id=%s"
			try:
				self.cursor.execute(cmd, (state1, state2, state3, user_id))
				self.conn.commit()
				return
			except:
				check_logger(user_id, self.logger, self.debug_mode)
				self.logger[user_id].error("Error set_state", exc_info=True)
				time.sleep(1)
				
	def add_user(self, user_id, username):
		"""Adds a new user to the database.

		Args:
			user_id: An integer representing the user's id.

		Returns:
			A string containing a message to the user. This string can be:
			- "Welcome to LingBot", if the user was not registered.
			- "Welcome back to LearnIt", if the user was already registered.
		"""
		tries = 20
		while tries > 0:
			tries -= 1
			try:
				self.cursor.execute("SELECT id from users WHERE id=%s;", (user_id, ))
				rows = self.cursor.fetchall()
				if(len(rows) > 0):
					return True
				self.cursor.execute("INSERT INTO users VALUES (%s, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, %s, DEFAULT);", (user_id, username))
				self.conn.commit()
				return True
			except:
				check_logger(user_id, self.logger, self.debug_mode)
				self.logger[user_id].error("Error add_user", exc_info=True)
				time.sleep(1)
				
		return False

	def get_known_users(self):
		"""Gets all the columns of all users in the database
		
		Returns:
			A list of tuples with the following information about the users:
			- An integer representing the user's id.
			- An integer representing the number of messages the user will receive per day.
			- An integer representing the current primary state of the user.
			- An integer representing the current secondary state of the user.
		"""
		tries = 5
		while tries > 0:
			tries -= 1
			cmd = "SELECT id FROM users;"
			try:
				known = set()
				self.cursor.execute(cmd)
				rows = self.cursor.fetchall()
				for row in rows:
					known.add(row[0])
				return known
			except:
				check_logger(user_id, self.logger, self.debug_mode)
				self.logger[user_id].error("Error get_known_users", exc_info=True)
				time.sleep(1)
				
		return set()

		

	def get_learning_words_limit(self, user_id):
		tries = 5
		while tries > 0:
			tries -= 1
			cmd = "SELECT learning_words_per_day from users WHERE id=%s;"
			try:
				self.cursor.execute(cmd, (user_id, ))
				rows = self.cursor.fetchall()
				if(len(rows) == 0):
					return 0
				return rows[0][0]
			except:
				check_logger(user_id, self.logger, self.debug_mode)
				self.logger[user_id].error("Error get_learning_words_limit", exc_info=True)
				time.sleep(1)
		return 0


	def get_review_cards_day_limit(self, user_id):
		tries = 5
		while tries > 0:
			tries -= 1
			cmd = "SELECT review_cards_per_day from users WHERE id=%s;"
			try:
				self.cursor.execute(cmd, (user_id, ))
				rows = self.cursor.fetchall()
				if(len(rows) == 0):
					return 0
				return rows[0][0]
			except:
				check_logger(user_id, self.logger, self.debug_mode)
				self.logger[user_id].error("Error get_review_cards", exc_info=True)
				time.sleep(1)
		return 0


	def set_card_waiting(self, user_id, card_id):
		tries = 20
		while tries > 0:
			tries -= 1
			cmd = "UPDATE users SET card_waiting=%s WHERE id=%s;"
			try:
				self.cursor.execute(cmd, (card_id, user_id))
				self.conn.commit()
				return
			except:
				check_logger(user_id, self.logger, self.debug_mode)
				self.logger[user_id].error("Error set_card_waiting", exc_info=True)
				time.sleep(1)
		return None

		


	def get_card_waiting(self, user_id):
		tries = 20
		while tries > 0:
			tries -= 1
			cmd = "SELECT card_waiting FROM users WHERE id=%s;"
			try:
				self.cursor.execute(cmd, (user_id, ))
				card = self.cursor.fetchall()
				if(len(card) == 0):
					return 0
				return card[0][0]
			except:
				check_logger(user_id, self.logger, self.debug_mode)
				self.logger[user_id].error("Error get_card_waiting", exc_info=True)
				time.sleep(1)

		return 0

	def get_grade_waiting(self, user_id):
		tries = 5
		while tries > 0:
			tries -= 1
			cmd = "SELECT grade_waiting_for_process from users WHERE id=%s;"
			try:
				self.cursor.execute(cmd, (user_id, ))
				rows = self.cursor.fetchall()
				if(len(rows) == 0):
					return None
				return rows[0][0]
			except:
				check_logger(user_id, self.logger, self.debug_mode)
				self.logger[user_id].error("Error get_grade_waiting", exc_info=True)
				time.sleep(1)
		return None




	def set_grade_waiting(self, user_id, grade):
		tries = 5
		while tries > 0:
			tries -= 1
			cmd = "UPDATE users SET grade_waiting_for_process=%s WHERE id=%s"
			try:
				self.cursor.execute(cmd, (grade, user_id))
				self.conn.commit()
				return
			except:
				check_logger(user_id, self.logger, self.debug_mode)
				self.logger[user_id].error("Error set_grade_waiting", exc_info=True)
				time.sleep(1)
		return None




	def get_card_waiting_type(self, user_id):
		tries = 5
		while tries > 0:
			tries -= 1
			cmd = "SELECT card_waiting_type from users WHERE id=%s;"
			try:
				self.cursor.execute(cmd, (user_id, ))
				rows = self.cursor.fetchall()
				if(len(rows) == 0):
					return 0
				return rows[0][0]
			except:
				check_logger(user_id, self.logger, self.debug_mode)
				self.logger[user_id].error("Error get_card_waiting_type", exc_info=True)
				time.sleep(1)

		return None

		

	def set_card_waiting_type(self, user_id, card_waiting_type):
		tries = 5
		while tries > 0:
			tries -= 1
			cmd = "UPDATE users SET card_waiting_type=%s WHERE id=%s"
			try:
				self.cursor.execute(cmd, (card_waiting_type, user_id))
				self.conn.commit()
				return 
			except:
				check_logger(user_id, self.logger, self.debug_mode)
				self.logger[user_id].error("Error set_card_waiting_type", exc_info=True)
				time.sleep(1)
		return None

	def get_cards_per_hour(self, user_id):
		tries = 5
		while tries > 0:
			tries -= 1
			cmd = "SELECT cards_per_hour from users WHERE id=%s;"
			try:
				self.cursor.execute(cmd, (user_id, ))
				rows = self.cursor.fetchall()
				if(len(rows) == 0):
					return 0
				return rows[0][0]
			except:
				check_logger(user_id, self.logger, self.debug_mode)
				self.logger[user_id].error("Error get_cards_per_hour", exc_info=True)
				time.sleep(1)

		return None

		

	def set_cards_per_hour(self, user_id, cards_per_hour):
		tries = 5
		while tries > 0:
			tries -= 1
			cmd = "UPDATE users SET cards_per_hour=%s WHERE id=%s"
			try:
				self.cursor.execute(cmd, (cards_per_hour, user_id))
				self.conn.commit()
				return 
			except:
				check_logger(user_id, self.logger, self.debug_mode)
				self.logger[user_id].error("Error set_cards_per_hour", exc_info=True)
				time.sleep(1)
		return None

	def get_active(self, user_id):
		tries = 5
		while tries > 0:
			tries -= 1
			cmd = "SELECT active from users WHERE id=%s;"
			try:
				self.cursor.execute(cmd, (user_id, ))
				rows = self.cursor.fetchall()
				if(len(rows) == 0):
					return 0
				return rows[0][0]
			except:
				check_logger(user_id, self.logger, self.debug_mode)
				self.logger[user_id].error("Error get_active", exc_info=True)
				time.sleep(1)
		return None

	def set_active(self, user_id, active):
		tries = 5
		while tries > 0:
			tries -= 1
			cmd = "UPDATE users SET active=%s WHERE id=%s"
			try:
				self.cursor.execute(cmd, (active, user_id))
				self.conn.commit()
				return 
			except:
				check_logger(user_id, self.logger, self.debug_mode)
				self.logger[user_id].error("Error set_active", exc_info=True)
				time.sleep(1)
		return None

	def get_id_by_username(self, username):
		tries = 20
		while tries > 0:
			tries -= 1
			cmd = "SELECT id from users WHERE username=%s;"
			try:
				self.cursor.execute(cmd, (username, ))
				rows = self.cursor.fetchall()
				if(len(rows) == 0):
					return None
				return rows[0][0]
			except:
				check_logger(user_id, self.logger, self.debug_mode)
				self.logger[user_id].error("Error get_id_by_username", exc_info=True)
				time.sleep(1)
		return None
			

	def get_public(self, user_id):
		tries = 5
		while tries > 0:
			tries -= 1
			cmd = "SELECT public from users WHERE id=%s;"
			try:
				self.cursor.execute(cmd, (user_id, ))
				rows = self.cursor.fetchall()
				if(len(rows) == 0):
					return 0
				return rows[0][0]
			except:
				check_logger(user_id, self.logger, self.debug_mode)
				self.logger[user_id].error("Error get_public", exc_info=True)
				time.sleep(1)
		return 0

	def get_username(self, user_id):
		tries = 5
		while tries > 0:
			tries -= 1
			cmd = "SELECT username from users WHERE id=%s;"
			try:
				self.cursor.execute(cmd, (user_id, ))
				rows = self.cursor.fetchall()
				if(len(rows) == 0):
					return 0
				return rows[0][0]
			except:
				check_logger(user_id, self.logger, self.debug_mode)
				self.logger[user_id].error("Error get_username", exc_info=True)
				time.sleep(1)
		return 0


	def set_public(self, user_id, public):
		tries = 5
		while tries > 0:
			tries -= 1
			cmd = "UPDATE users SET public=%s WHERE id=%s"
			try:
				self.cursor.execute(cmd, (public, user_id))
				self.conn.commit()
				return 
			except:
				check_logger(user_id, self.logger, self.debug_mode)
				self.logger[user_id].error("Error set_public", exc_info=True)
				time.sleep(1)
		return None



		
