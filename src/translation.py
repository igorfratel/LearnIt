
def translate(txt, language):
	return message[txt][language]

native_languages = {'English': 0,
					'Português': 1}

native_languages_map = {0: 'English',
						1: 'Português'}

poll_text = ("*5* - _perfect response, without any hesitation_\n" +
					 "*4* - _correct response after a hesitation_\n" +
					 "*3* - _correct response recalled with difficulty_\n" + 
					 "*2* - _incorrect response; where the correct one seemed easy to recall_\n" + 
					 "*1* - _incorrect response; the correct one was remembered_\n" +
					 "*0* - _complete blackout._")

poll_text_pt = ("*5* - _resposta perfeita, sem qualquer hesitação_\n" +
				 "*4* - _resposta correta, mas com certa hesitação_\n" +
				 "*3* - _resposta correta, lembrada com dificuldade_\n" + 
				 "*2* - _resposta incorreta; a resposta certa era fácil de lembrar_\n" + 
				 "*1* - _resposta incorreta; a resposta certa foi lembrada agora_\n" +
				 "*0* - _total esquecimento._")

help_msg = ("Use the command /add\_item to add items you are interested in learning " + 
			"or just use the command /copy\_from\_user to copy items from other users. " +
			"During any process you can use /cancel to cancel the ongoing events, if you made a mistake, for example.\n" +
		   "If you have questions or want to support the project, please contact one of the developers:" +
		   "\n*Tiago Napoli*\nTelegram: t.me/tiagonapoli\nEmail: napoli.tiago@hotmail.com\n" + 
		   "\n*Gabriel Camargo*\nTelegram: t.me/gabriel\_camargo\nEmail: gacamargo1.000@gmail.com\n")

help_msg_pt = ("Use o comando /add\_item para adicionar itens que você está interessado em aprender " +
			"ou use /copy\_from\_user para copiar cards prontos de outros usuários. Durante qualquer processo, use /cancel para cancelar qualquer evento, se você cometeu algum erro, por exemplo" +
		   "Se você tiver dúvidas, sugestões ou quiser apoiar o projeto, contate um dos desenvolvedores:" +
		   "\n*Tiago Napoli*\nTelegram: t.me/tiagonapoli\nEmail: napoli.tiago@hotmail.com\n" + 
		   "\n*Gabriel Camargo*\nTelegram: t.me/gabriel\_camargo\nEmail: gacamargo1.000@gmail.com\n")

welcome = ("Use the command /add\_item to add items you are interested in learning " +
			"or just use the command /copy\_from\_user to copy items from other users. During any process you can use /cancel to cancel the ongoing events, if you made a mistake, for example.")

welcome_pt = ("Use o comando /add\_item para adicionar itens que você está interessado em aprender " +
			"ou use /copy\_from\_user para copiar cards prontos de outros usuários. Durante qualquer processo, use /cancel para cancelar qualquer evento, se você cometeu algum erro, por exemplo")

message = { "#setup_user_username_error":
				{0: "Please, create your Telegram Username first. You just have to go to Settings->Info->Username to create it. After you create one, type /start again.\nPor favor, crie seu nome de usuário Telegram primeiro. Vá até às configurações do Telegram->Informações->Nome de usuário. Depois de criar, digite /start novamente.",
				 1: "Please, create your Telegram Username first. You just have to go to Settings->Info->Username to create it. After you create one, type /start again.\nPor favor, crie seu nome de usuário Telegram primeiro. Vá até às configurações do Telegram->Informações->Nome de usuário. Depois de criar, digite /start novamente."}	,	

			"#welcome_back":
				{0: "Welcome back to LearnIt!" + "\n" + welcome,
				 1: "Bem-vindo de volta ao LearnIt!" + "\n" + welcome_pt},

			"#setup_user_mother_language":
				{0: "*Please select your mother language:*\n*Por favor, selecione sua língua nativa:*",
				 1: "*Please select your mother language:*\n*Por favor, selecione sua língua nativa:*"},

			"#setup_user_choose_from_keyboard":
				{0: "Please choose from keyboard.\nPor favor, selecione do teclado fornecido.",
				 1: "Please choose from keyboard.\nPor favor, selecione do teclado fornecido."},

			"#welcome":
				{0: "Welcome to LearnIt!" + "\n" + welcome,
				 1: "Bem-vindo ao LearnIt!" + "\n" + welcome_pt},

			"#cancel": 
				{0: "_Canceled..._",
				 1: "_Cancelado..._"},

			"#user_dont_exist_error_handling": 
				{0: "LearnIt is under development, so sometimes we have to do some experiments and reset some things, maybe because of this, your user isn't in our database. To fix this, please send a /start",
				 1: "LearnIt está em desenvolvimento, por isso algumas vezes nós fazemos alguns experimentos e reiniciamos certas coisas, talvez por isso seu usuário não esteja em nosso banco de dados. Para consertar, envie-me /start"},

			"#message_not_understood":
				{0: "Oops, didn't understand your message '%s' (use /cancel if you need)...",
				 1: "Oops, não entendi sua mensagem '%s' (se precisar, use /cancel)..."},

			"#help_msg": 
				{0: help_msg,
				 1: help_msg_pt},

			"#reset_all_states_exception":
				{0: "An error in the server ocurred, the operation was canceled",
				 1: "Um erro no servidor ocorreu, a operação foi cancelada"},

			"#stop_msg":
				{0: "You will *not* receive any card until you use the command /start again",
				 1: "Você *não* receberá nenhum cartão até que use o comando /start novamente"},

			"#settings_msg": 
				{0: "*Which settings do you want to change?*",
				 1: "*Qual configuração você deseja mudar?*"},

			"#choose_from_keyboard":
				{0: "Please choose from keyboard",
				 1: "Por favor, selecione do teclado fornecido"},

			"#settings_cards_per_hour": 
				{0: "*How many cards you want to receive per hour?*",
				 1: "*Quantos cartões deseja receber por hora?*"},

			"#settings_change_language":
				{0: "*Please select your mother language:*",
				 1: "*Por favor, selecione sua língua nativa:*"},

			"#settings_set_public": 
				{0: 'Your profile is now public',
				 1: 'Seu perfil é agora público'},

			"#settings_set_private": 
				{0: 'Your profile is now private',
				 1: 'Seu perfil é agora privado'},

			"#settings_cards_per_hour_setted": 
				{0: "_Cards per hour set successfully!_",
				 1: "_Cartões por hora alterados com sucesso!_"},

			"#settings_language_setted":
				{0: "_Bot language changed sucessfully!_",
				 1: "_Idioma do bot alterado com sucesso!_"},

			"#add_item_subject_intro":
				{0: "*Send the item subject*. You can send a *new subject* or *select from existing*",
				 1: "*Envie-me a matéria do item a adicionar*. Você pode mandar uma *nova matéria* ou *selecionar das existentes*"},

			"#add_item_no_subjects":
				{0: "_There are no subjects registered yet, please send a new subject..._",
				 1: "_Não há matérias cadastradas ainda, por favor envie uma nova matéria..._"},

			"#list_subjects": 
				{0: "Subjects registered:",
				 1: "Matérias cadastradas:"},	

			"#item_subject":
				{0: "Item's subject: *%s*",
				 1: "Matéria do item: *%s*"},

			"#item_topic":
				{0: "Item's topic: *%s*",
				 1: "Tópico do item: *%s*"},

			"#study_item":
				{0: "*Study item:* _%s_",
				 1: "*Item de estudo:* _%s_"},


			"#add_item_topic_intro": 
				{0: "*Send the item's topic*. You can send a *new topic* or *select from existing*",
				 1: "*Envie-me o tópico do item*. Você pode mandar um *novo tópico* ou *selecionar dos existentes*"},	

			"#list_topics": 
				{0: "_Topics registered:_",
				 1: "_Tópicos registrados:_"},	

			"#add_item_no_topics": 
				{0: "_There are no topics registered in this subject yet, so please_ *send a new topic*",
				 1: "_Não há tópicos registrados nessa matéria ainda. Por favor,_ *envie-me um novo tópico*"},

			"#character_exceeded":
				{0: "Please, don't exceed %s characters. You digited %s characters. Send the language again:",
				 1: "Por favor, não exceda %s caracteres. Você digitou %s caracteres. Me envie a linguagem novamente:"},

			"#character_null": 
				{0: "Please, don't use / or \ or _ or *. Send the language again:",
				 1: "Por favor, não use / ou \ ou _ ou *. Me envie a linguagem novamente:"},

			"#add_item_initial_hint":
				{0: "_Hint: The process to add a word is way easier on Telegram Desktop_",
				 1: "_Dica: O processo para adicionar palavra é muito mais fácil e rápido no Telegram Desktop_"},

			"#add_item_ask_study_item":
				{0: "*Send item to add* (in _%s_)",
				 1: "*Me envie o item a adicionar* (em _%s_)"},	

			"#add_item_get_study_item_1":						
				{0: "_Please,_ *send an image* _to use instead of a text:_",
				 1: "_Por favor,_ *me envie uma imagem* _ para ser usada ao invés de um texto:_"},

			"#add_item_study_item_already_exists":
				{0: "This item is already registered, if you want to add it anyway, please, erase it first. The process will be canceled",
				 1: "Esse item já está registrado. Se você quer adicioná-lo mesmo assim, por favor, delete-lo primeiro. O processo atual será cancelado"},	

			'Send image': 
				{0: 'Send image',
				 1: 'Enviar imagem'},	

			'Send audio': 
				{0: 'Send audio',
				 1: 'Enviar audio'},	

			'Send text': 
				{0: 'Send text',
				 1: 'Enviar texto'},	

			'End selection': 
				{0: 'End selection',
				 1: 'Terminar seleção'},

			'Go back':
				{0: 'Go back',
				 1: 'Voltar'},

			"#add_item_relate_menu":
				{0: "_Select the ways you want to relate to the item (one or more):_",
				 1: "_Selecione os meios com que você quer relacionar o item (um ou mais)_"},	
		
			"#add_item_relate_menu_empty": 
				{0: "_Please, select_ *at least one way* _to relate to the item:_",
				 1: "_Por favor, selecione_ *pelo menos um meio* _com o qual relacione seu item:_"},

			"#ask_to_send_image":
				{0: "Send *an image*:",
				 1: "Envie *uma imagem*:"},

			"#send_image_hint":
				{0: "_Use_ @pic _<image_\__name> or_ @bing _<image_\__name> to select an image_",
				 1: "_Use_ @pic _<termos_\__para_\__pesquisa> ou_ @bing _<termos_\__para_\__pesquisa> para selecionar uma imagem_"},

			"#ask_to_send_audio":
				{0: "Send *an audio*:",
				 1: "Envie *um áudio*:"},

			"#send_audio_hint":
				{0: "_Hint: You can download pronunciations on forvo.com and then send them to me. This process is way easier on PC (Telegram Desktop)_",
				 1: "_Dica: Você pode baixar pronúncias do site forvo.com e então mandá-las para mim. Esse processo é muito mais fácil no PC (Telegram Desktop)_"},	

			"#ask_to_send_text":
				{0: "Send *a text*:",
				 1: "Envie *uma mensagem de texto*:"},

			"#success": 
				{0: "_Successfully done!_",
				 1: "_Sucesso!_"},	

			"#audio_received": 
				{0: "_Audio received successfuly_",
				 1: "_Audio recebido com sucesso_"},

			"#image_received": 
				{0: "_Image received successfuly_",
				 1: "_Imagem recebida com sucesso_"},

			"#text_received": 
				{0: "_Text received successfuly_",
				 1: "_Texto recebido com sucesso_"},

			"#add_item_ask_more_items":
				{0: "_Would you like to add more items in_ *%s*_, in topic_ *%s*_?_",
				 1: "_Você gostaria de adicionar mais itens em_ *%s*_, no tópico_ *%s*_?_"},

			'Yes': 
				{0: 'Yes',
				 1: 'Sim'},

			'No': 
				{0: 'No',
				 1: 'Não'},

			"#ok":
				{0: "_OK!_",
				 1: "_OK!_"},

			"#add_item_active_success":
				{0: "_The item was successfully added. It's_ *active* _for training._",
				 1: "_O item foi adicionado com sucesso. Está_ *ativo* _para treinamento._"},

			"#add_item_unactive_success":
				{0: "_The item was successfully added, but it's_ *unactive* _for training, since the topic or subject it was added on is unactive._",
				 1: "_O item foi adicionado com sucesso, mas está_ *inativo* _para treinamento, já que o tópico ou matéria em que foi adicionado está inativo._"},

			"#no_active_subjects":
				{0: "_There are no active subjects. Nothing to list..._",
				 1: "_Não há matérias ativas. Nada para listar..._"},

			"#no_active_topics":
				{0: "_There are no active topics in this subject. Nothing to list..._",
				 1: "_Não há tópicos ativos nesta matéria. Nada para listar..._"},

			"#list_subject_selection":
				{0: "_Active or partially active_ *subjects*. Select one for more detail.",
				 1: "*Matérias* _ativas ou parcialmente ativas_. Selecione uma delas para mais detalhes."},

			"#list_topic_selection":
				{0: "_Active or partially active_ *topics*. Select one for more detail.",
				 1: "*Tópicos* _ativos ou parcialmente ativos_. Selecione um deles para mais detalhes."},

			"#list_study_item_selection":
				{0: "_Active_ *study items*. Select one for more detail.",
				 1: "*Itens* _de estudo ativos_. Selecione um deles para mais detalhes."},

			"#no_subjects":
				{0: "_There are no subjects registered yet..._",
				 1: "_Não há matérias cadastradas ainda..._"},

			"#subject_selection":
				{0: "_Select the subject:_",
				 1: "_Selecione a matéria:_"},

			"#topic_selection":
				{0: "_Select the topic:_",
				 1: "_Selecione o tópico:_"},

			"#review_select_topics":
				{0: "_Select the topics to review:_",
				 1: "_Selecione os tópicos a revisar:_"},
				
			"#review_select_topics_empty":
				{0: "_Select_ *at least one* _topic to review:_",
				 1: "_Selecione_ *pelo menos um* _tópico a revisar:_"},

			"#review_card_number":
				{0: "_Select how many cards you want to receive:_",
				 1: "_Selecione quantas cartas deseja receber:_"},		

			"#image_question": 
				{0: "*Image answer:*",
				 1: "*Resposta com imagem:*"},

			"#audio_question": 
				{0: "*Audio answer:*",
				 1: "*Resposta com áudio:*"},

			"#text_question": 
				{0: "*Text answer:*",
				 1: "*Resposta com texto:*"},

			"#card_type": 
				{0: "*%s card%s!*",
				 1: "*Cartão de %s %s!*"},

			"#answer_type_1": 
				{0: "*Answer:* ",
				 1: "*Resposta:* "},

			"#answer_type_0":
				{0: "*Answer:* _%s_",
				 1: "*Resposta:* _%s_"},

			"#card_query_study_type_1": 
				{0: "Try to relate the next message to something you know in *%s/%s*. When you remeber or when you are ready, *send me any message*",
				 1: "Tente relacionar a próxima mensagem com algo que você aprendeu em *%s/%s*. Quando você lembrar ou estiver pronto, *envie-me qualquer mensagem*"},

			"#card_query_audio": 
				{0: "Transcribe the audio in _%s_, topic _%s_",
				 1: "Transcreva o áudio em _%s_, tópico _%s_"},

			"#card_query_text": 
				{0: "Relate the text to something in _%s_, topic _%s_",
				 1: "Relacione o texto a algo em _%s_, tópico _%s_"},

			"#card_query_image":
				{0: "Relate the image to something in _%s_, topic _%s_",
				 1: "Relacione a imagem a algo em _%s_, tópico _%s_"},

			"#correct_answer": 
				{0: "_That was correct!_",
				 1: "_Correto!_"},

			"#incorrect_answer": 
				{0: "_There was a mistake in your answer_ :(",
				 1: "_Houve um erro na sua resposta_ :("},

			"#review_done": 
				{0: "*Review session done!*",
				 1: "*Revisão terminada!*"},

			"#grade_your_performance": 
				{0: "_Please grade your performance to answer the card_\n",
				 1: "_Por favor, dê uma nota à sua performance para responder o cartão_\n"},

			"#poll_text": 
				{0: poll_text,
				 1: poll_text_pt},

			"#copy_get_telegram_username":
				{0: 'Please, send the Telegram username of the user you want to copy some words from',
				 1: 'Por favor, envie o nome de usuário Telegram da pessoa que você quer copiar palavras'},

			"#invalid_username": 
				{0: "Invalid username. Please, if you still want to copy from a user, send /copy\_from\_user again.",
				 1: "Usuário inválido. Se você ainda quer copiar de algum usuário, me envie /copy\_from\_user novamente."},

			"#invalid_yourself_username": 
				{0: "You can't copy from yourself! Please, if you still want to copy from a user, send /copy\_from\_user again.",
				 1: "Você não pode copiar de si mesmo! Se você ainda quer copiar de algum usuário, me envie /copy\_from\_user novamente."},

			"#invalid_private_username": 
				{0: "This user is not public. Please, if you still want to copy from a user, send /copy\_from\_user again.",
				 1: "Esse usuário não é público. Se você ainda quer copiar de algum usuário, me envie /copy\_from\_user novamente."},
	
			"#copy_no_subjects": 
				{0: "The user _%s_ does not have any subjects",
				 1: "O usuário _%s_ não tem nenhuma matéria registrada"},
						
			'#overwritten_items': 
				{0: '*Overwritten items:*',
				 1: '*Itens sobrescritos:*'},

			'#copied_items': 
				{0: '*New copied items:*',
				 1: '*Novos itens copiados:*'},

			'#copy_results': 
				{0: '*Copy results:*',
				 1: '*Resultados da cópia:*'},
		
			'#topic':
				{0: "*Topic:* _%s_",
				 1: "*Tópico:* _%s_"},

			"#no_overwritten_items": 
				{0: 'There were no overwritten words!',
				 1: 'Não houve palavras sobrescritas!'},

			"#ask_overwrite":
				{0: "In case some words to be copied already exist in your words, *should we overwrite?* If you already copied from this user and topic maybe you don't want to overwrite _(If we overwrite you lose all learning data about that word)_",
				 1: "Em caso alguma palavra a ser copiada já exista na sua lista, eu *deveria sobrescrever?* Se você já copiou desse usuário e tópico talvez você não queira sobrescrever_(Se sobrescrever você perde todos os dados de aprendizado daquela palavra)_"},

			"#copy_select_topics": 
				{0: "Select the topics you want to copy:",
				 1: "Selecione os tópicos que você deseja copiar:"},

			'Subjects': 
				{0: "Subjects",
				 1: "Matérias"},

			'Topics':
				{0: "Topics",
				 1: "Tópicos"}, 

			'Study Items':
				{0: "Study Items",
				 1: "Itens de estudo"},

			"#ask_what_to_erase":
				{0: "What would you like to erase?",
				 1: "O que você gostaria de apagar?"},
		
			"#erase_select_study_items":
				{0: "Select the items you want to erase:",
				 1: "Selecione os itens que deseja apagar:"}, 

			"#erase_select_topics":
				{0: "Select the topics you want to erase:",
				 1: "Selecione os tópicos que deseja apagar:"}, 

			"#erase_select_subjects":
				{0: "Select the subjects you want to erase:",
				 1: "Selecione as matérias que deseja apagar:"}, 

			"#items_erased":
				{0: "*Items erased:*",
				 1: "*Itens apagados:*"}, 

			"#topics_erased":
				{0: "*Topics erased:*",
				 1: "*Tópicos apagados:*"}, 

			"#subjects_erased":
				{0: "*Subjects erased:*",
				 1: "*Matérias apagadas:*"},

			'Cards per hour':
				{0: "Cards per hour",
				 1: "Cartões por hora"},

			'Set profile public': 
				{0: "Set profile public",
				 1: "Tornar perfil público"},

			'Set profile private':
				{0: "Set profile private",
				 1: "Tornar perfil privado"},

			'Change bot language':
				{0: "Change bot language",
				 1: "Trocar o idioma do bot"},

			'#bot_turn_off':
				{0: "The bot is restarting, the operation is being canceled. Sorry for the inconvenience.",
				 1: "O bot está sendo reiniciado, a operação será cancelada. Desculpe pela inconveniência."},

			"#select_training_select_topics":
				{0: "_Select the topics you want to be active for your training (Unselected will be unactive):__",
				 1: "_Selectione os tópicos que deseja que fiquem ativos para treinamento (Os não selecionados ficarão inativos:_"},

			"#active_topics_listing":
				{0: "_Active topics on %s:_",
				 1: "_Tópicos ativos em %s:_"},

			"#no_active_topics":
				{0: "*There are no active topics*",
				 1: "*Não há tópicos ativos*"},

			"#too_much_time_waiting_ans":
				{0: "Oops, maybe you forgot to answer the card. This will be canceled, maybe you will receive a new one in the future :)",
				 1: "Oops, talvez você se esqueceu de responder o cartão. Ele será cancelado, talvez você recebe um novo em breve :)"},

			"#too_much_time_on_menu":
				{0: "Oops, maybe you forgot to quit this menu, we will do that for you...",
				 1: "Oops, talvez você se esqueceu de sair desse menu, vamos fazer isso por você..."},

			"#ask_for_audio":
				{0: "Do you want to receive audios?",
				 1 : "Você gostaria de receber audios?"},

			"#review_length":
				{0: "There are %s review cards in total",
				 1 : "Total de cards: %s"},

			'#all_cards':
				{0: "All cards",
				 1 : "Todos os cards"}

}