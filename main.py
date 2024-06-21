import pyautogui
import time

search_region = (2973, 111, 3730, 1621)

def find_lowest_image(image_path, region=search_region):
    # Locate all instances of the image on the screen
    locations = list(pyautogui.locateAllOnScreen(image_path, confidence=0.9, region=search_region))
    
    if not locations:
        print("Image not found on the screen.")
        return None
    
    # Find the location with the maximum 'top' value
    lowest_location = max(locations, key=lambda loc: loc.top)
    
    return lowest_location

def next():
    time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen("check_btn.png", region=search_region, confidence=0.9))
    time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen("green_continue_btn.png", region=search_region, confidence=0.9))

while True:
    cant_listen_now_pos = pyautogui.locateCenterOnScreen("cant_listen_now_btn.png", region=search_region)
    if cant_listen_now_pos is not None:
        pyautogui.click(cant_listen_now_pos)
        time.sleep(1)
        pyautogui.click(pyautogui.locateCenterOnScreen("orange_continue_btn.png", region=search_region, confidence=0.9))
        continue
    
    cant_listen_now_pos = pyautogui.locateCenterOnScreen("check_btn.png", region=search_region)
    if cant_listen_now_pos is not None:
        pyautogui.click(cant_listen_now_pos)
        continue
    
    cant_speak_now_pos = pyautogui.locateCenterOnScreen("cant_speak_now_btn.png", region=search_region)
    if cant_speak_now_pos is not None:
        pyautogui.click(cant_speak_now_pos)
        time.sleep(1)
        pyautogui.click(pyautogui.locateCenterOnScreen("orange_continue_btn.png", region=search_region))
        continue
    
    green_continue_pos = pyautogui.locateCenterOnScreen("green_continue_btn.png", region=search_region, confidence=0.9)
    if green_continue_pos is not None:
        pyautogui.click(green_continue_pos)
        continue
    
    close_subscription_pos = pyautogui.locateCenterOnScreen("close_subscription.png", region=search_region)
    if close_subscription_pos is not None:
        pyautogui.click(close_subscription_pos)
        continue
    
    blue_continue_btn_pos = pyautogui.locateCenterOnScreen("blue_continue_btn.png", region=search_region, confidence=0.9)
    if blue_continue_btn_pos is not None:
        pyautogui.click(blue_continue_btn_pos)
        continue
    
    blue_continue_btn_pos = pyautogui.locateCenterOnScreen("claim_reward_btn.png", region=search_region, confidence=0.9)
    if blue_continue_btn_pos is not None:
        pyautogui.click(blue_continue_btn_pos)
        continue
    
    blue_continue_btn_pos = pyautogui.locateCenterOnScreen("wite_orange_continue_btn.png", region=search_region, confidence=0.9)
    if blue_continue_btn_pos is not None:
        pyautogui.click(blue_continue_btn_pos)
        continue
    
    continue_without_reminders_btn_pos = pyautogui.locateCenterOnScreen("continue_without_reminders_btn.png", region=search_region)
    if continue_without_reminders_btn_pos is not None:
        pyautogui.click(continue_without_reminders_btn_pos)
        continue
    
    maybe_later_btn_pos = pyautogui.locateCenterOnScreen("maybe_later_btn.png", region=search_region)
    if maybe_later_btn_pos is not None:
        pyautogui.click(maybe_later_btn_pos)
        continue
    
    got_it_btn_pos = pyautogui.locateCenterOnScreen("got_it_btn.png", region=search_region)
    if got_it_btn_pos is not None:
        pyautogui.click(got_it_btn_pos)
        continue
    
    practice_to_earn_hearts_btn_pos = pyautogui.locateCenterOnScreen("practice_to_earn_hearts_btn.png", region=search_region, confidence=0.9)
    if practice_to_earn_hearts_btn_pos is not None:
        pyautogui.click(practice_to_earn_hearts_btn_pos)
        continue
    
    if pyautogui.locateCenterOnScreen("the_man_exercise.png", region=search_region, confidence=0.9) is not None:
        pyautogui.click(pyautogui.locateCenterOnScreen("l_btn.png", region=search_region))
        pyautogui.click(pyautogui.locateCenterOnScreen("type_in_french_input.png", region=search_region, confidence=0.9))
        pyautogui.write("homme")

        next()
        continue
    
    if pyautogui.locateCenterOnScreen("the_cat_exercise.png", region=search_region, confidence=0.9) is not None:
        pyautogui.click(pyautogui.locateCenterOnScreen("le_btn.png", region=search_region))
        pyautogui.click(pyautogui.locateCenterOnScreen("type_in_french_input.png", region=search_region, confidence=0.9))
        pyautogui.write("chat")

        next()
        continue
    
    if pyautogui.locateCenterOnScreen("the_boy_exercise.png", region=search_region, confidence=0.9) is not None:
        pyautogui.click(pyautogui.locateCenterOnScreen("le_btn.png", region=search_region))
        pyautogui.click(pyautogui.locateCenterOnScreen("type_in_french_input.png", region=search_region, confidence=0.9))
        pyautogui.write("garcon")

        next()
        continue
    
    if pyautogui.locateCenterOnScreen("one_exercise.png", region=search_region, confidence=0.9) is not None:
        pyautogui.click(pyautogui.locateCenterOnScreen("type_in_french_input.png", region=search_region))
        pyautogui.write("un")

        next()
        continue
    
    if pyautogui.locateCenterOnScreen("select_the_correct_translation_title.png", region=search_region, confidence=0.9) is not None:
        if pyautogui.locateCenterOnScreen("man_exercise.png", region=search_region) is not None:
            pyautogui.click(pyautogui.locateCenterOnScreen("man_anser.png", region=search_region, confidence=0.9))

            next()
            continue
        
        if pyautogui.locateCenterOnScreen("boy_question.png", region=search_region) is not None:
            pyautogui.click(pyautogui.locateCenterOnScreen("garcon_big_btn.png", region=search_region, confidence=0.9))

            next()
            continue
        
        if pyautogui.locateCenterOnScreen("cat_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.locateCenterOnScreen("chat_big_btn.png", region=search_region, confidence=0.9))

            next()
            continue
        
        if pyautogui.locateCenterOnScreen("and_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.locateCenterOnScreen("et_big_btn.png", region=search_region, confidence=0.9))

            next()
            continue
        
        if pyautogui.locateCenterOnScreen("a_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.locateCenterOnScreen("un_big_btn.png", region=search_region, confidence=0.9))

            next()
            continue
        
        continue
    
    if pyautogui.locateCenterOnScreen("complete_the_sentence_title.png", region=search_region, confidence=0.9) is not None:
        if pyautogui.locateCenterOnScreen("a_man_and_a_boy_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("un_homme_input.png", region=search_region)))
            pyautogui.write("et un garcon")

            next()
            continue
        
        if pyautogui.locateCenterOnScreen("a_cat_and_a_man_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("un_chat_input.png", region=search_region)))
            pyautogui.write("et un homme")

            next()
            continue
        
        if pyautogui.locateCenterOnScreen("a_boy_and_a_cat_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("un_garcon_input.png", region=search_region)))
            pyautogui.write("et un chat")

            next()
            continue
        
        if pyautogui.locateCenterOnScreen("a_cat_and_a_boy.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("un_chat_input.png", region=search_region)))
            pyautogui.write("et un garcon")

            next()
            continue
        
        if pyautogui.locateCenterOnScreen("a_man_and_a_cat_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("un_homme_input.png", region=search_region)))
            pyautogui.write("et un chat")

            next()
            continue
        
        continue
        
    if pyautogui.locateCenterOnScreen("complete_the_translation_title.png", region=search_region, confidence=0.9) is not None:
        if pyautogui.locateCenterOnScreen("a_cat_and_a_boy.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("un_chat_et_un_input.png", region=search_region)))
            pyautogui.write("garcon")

            next()
            continue
        
        if pyautogui.locateCenterOnScreen("a_cat_and_a_man_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("un_chat_et_un_input.png", region=search_region)))
            pyautogui.write("homme")

            next()
            continue
        
        if pyautogui.locateCenterOnScreen("a_man_and_a_boy_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("un_homme_et_un_input.png", region=search_region)))
            pyautogui.write("garcon")

            next()
            continue
        
        if pyautogui.locateCenterOnScreen("a_boy_and_a_cat_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("un_garcon_et_un_input.png", region=search_region)))
            pyautogui.write("chat")

            next()
            continue
        
        if pyautogui.locateCenterOnScreen("a_man_and_a_cat_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("un_homme_et_un_input.png", region=search_region)))
            pyautogui.write("chat")

            next()
            continue
        
        continue
        
    if pyautogui.locateCenterOnScreen("translate_this_sentence_title.png", region=search_region, confidence=0.9) is not None:
        text_pos = pyautogui.locateCenterOnScreen("type_the_french_translation.png", region=search_region, confidence=0.9)
        if text_pos is not None:
            if pyautogui.locateCenterOnScreen("a_man_and_a_cat_question.png", region=search_region, confidence=0.9) is not None:
                pyautogui.click(text_pos)
                pyautogui.write("un homme et un chat")

                next()
                continue
            
            if pyautogui.locateCenterOnScreen("a_man_question.png", region=search_region, confidence=0.9) is not None:
                pyautogui.click(text_pos)
                pyautogui.write("un homme")

                next()
                continue
            
            if pyautogui.locateCenterOnScreen("a_boy_question.png", region=search_region, confidence=0.9) is not None:
                pyautogui.click(text_pos)
                pyautogui.write("un garcon")

                next()
                continue
            
            if pyautogui.locateCenterOnScreen("a_boy_and_a_cat_question.png", region=search_region, confidence=0.9) is not None:
                pyautogui.click(text_pos)
                pyautogui.write("un garcon et un chat")

                next()
                continue
            
            if pyautogui.locateCenterOnScreen("a_man_and_a_boy_question.png", region=search_region, confidence=0.9) is not None:
                pyautogui.click(text_pos)
                pyautogui.write("un homme et un garcon")

                next()
                continue
            
            if pyautogui.locateCenterOnScreen("a_cat_and_a_boy.png", region=search_region, confidence=0.9) is not None:
                pyautogui.click(text_pos)
                pyautogui.write("un chat et un garcon")

                next()
                continue
            
            if pyautogui.locateCenterOnScreen("a_cat_and_a_man_question.png", region=search_region, confidence=0.9) is not None:
                pyautogui.click(text_pos)
                pyautogui.write("un chat et un homme")

                next()
                continue
            
            if pyautogui.locateCenterOnScreen("a_cat_question.png", region=search_region, confidence=0.9) is not None:
                pyautogui.click(text_pos)
                pyautogui.write("un chat")

                next()
                continue
            
            continue
        
        pos = pyautogui.locateCenterOnScreen("green_continue_btn.png", region=search_region, confidence=0.9)
        if pos is not None:
            pyautogui.click(pos)
            continue
        
        pos = pyautogui.locateCenterOnScreen("tap_to_see_word_bank_text.png", region=search_region, confidence=0.9)
        if pos is not None:
            pyautogui.click(pos)
            time.sleep(1)
        
        if pyautogui.locateCenterOnScreen("un_garcon_et_un_chat_exercice.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("a_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("boy_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("and_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("a_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("cat_small_btn.png", region=search_region)))

            next()
            continue
        
        if pyautogui.locateCenterOnScreen("un_garcon_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("a_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("boy_small_btn.png", region=search_region)))

            next()
            continue
        
        if pyautogui.locateCenterOnScreen("un_homme_et_un_garcon_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("a_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("man_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("and_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("a_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("boy_small_btn.png", region=search_region)))

            next()
            continue
        
        if pyautogui.locateCenterOnScreen("un_chat_et_un_garcon_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("a_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("cat_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("and_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("a_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("boy_small_btn.png", region=search_region)))

            next()
            continue
        
        if pyautogui.locateCenterOnScreen("a_man_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("un_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("homme_small_btn.png", region=search_region)))

            next()
            continue
        
        if pyautogui.locateCenterOnScreen("un_homme_et_un_chat_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("a_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("man_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("and_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("a_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("cat_small_btn.png", region=search_region)))
            next()
            continue
        
        if pyautogui.locateCenterOnScreen("a_boy_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("un_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("garcon_small_btn.png", region=search_region)))
            next()
            continue
        
        if pyautogui.locateCenterOnScreen("un_homme_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("a_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("man_small_btn.png", region=search_region)))
            next()
            continue
        
        if pyautogui.locateCenterOnScreen("a_cat_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("un_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("chat_small_btn.png", region=search_region)))
            next()
            continue
        
        if pyautogui.locateCenterOnScreen("a_boy_and_a_cat_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("un_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("garcon_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("et_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("un_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("chat_small_btn.png", region=search_region)))
            next()
            continue
        
        if pyautogui.locateCenterOnScreen("un_chat_et_un_homme.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("a_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("cat_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("and_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("a_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("man_small_btn.png", region=search_region)))
            next()
            continue
        
        if pyautogui.locateCenterOnScreen("a_cat_and_a_boy.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("un_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("chat_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("et_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("un_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("garcon_small_btn.png", region=search_region)))
            next()
            continue
        
        if pyautogui.locateCenterOnScreen("un_chat_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("a_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("cat_small_btn.png", region=search_region)))
            next()
            continue
        
        if pyautogui.locateCenterOnScreen("a_man_and_a_cat_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("un_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("homme_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("et_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("un_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("chat_small_btn.png", region=search_region)))
            next()
            continue
        
        if pyautogui.locateCenterOnScreen("a_man_and_a_boy_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("un_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("homme_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("et_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("un_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("garcon_small_btn.png", region=search_region)))
            next()
            continue
        
        if pyautogui.locateCenterOnScreen("a_cat_and_a_man_question.png", region=search_region, confidence=0.9) is not None:
            pyautogui.click(pyautogui.center(find_lowest_image("un_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("chat_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("et_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("un_small_btn.png", region=search_region)))
            pyautogui.click(pyautogui.center(find_lowest_image("homme_small_btn.png", region=search_region)))
            next()
            continue
        
        continue
    