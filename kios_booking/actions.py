from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Action,Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, AllSlotsReset, FollowupAction, Restarted
import re
import string
import json
import time
import re

class ActionRestarted(Action):
    """ This is for restarting the chat"""

    def name(self):
        return "action_chat_restart"

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]

class ChooseDink(FormAction):
    def name(self) -> Text:
        return "choose_dink_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["choose_drink"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "choose_drink": [self.from_text()],
        }
    def validate_choose_drink(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate verifyinfor value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'water':
            return {"choose_drink": "1"}
        elif intent == 'tea':
            return {"choose_drink": "2"}
        else:
            return {"choose_drink": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        return [FollowupAction("choose_food_form")]
class ChooseFood(FormAction):
    def name(self) -> Text:
        return "choose_food_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["choose_food"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "choose_food": [self.from_text()],
        }
    def validate_choose_food(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate verifyinfor value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'hoaqua':
            return {"choose_food": "3"}
        elif intent =='sukem':
            return {"choose_food": "4"}
        else:
            return {"choose_food": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        intent = tracker.get_slot("choose_food")
        dispatcher.utter_message(text="chọn | {}".format(intent))
        return [FollowupAction("action_chat_restart")]