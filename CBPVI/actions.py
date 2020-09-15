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
class RequestForm(FormAction):
    def name(self) -> Text:
        return "resquest_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["request"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "request": [self.from_text()],
        }
    def validate_request(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate request value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'register' or intent == 'advice':
            return {"request": intent}
        else:
            return {"request": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        intent = tracker.get_slot("request")
        if intent == 'register'
            return [FollowupAction("register_form")]
        elif intent == 'advice':
            return [FollowupAction("advice_form")]
        else:
            return []
class AdviceForm(FormAction):
    def name(self) -> Text:
        return "advice_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["advice"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "advice": [self.from_text()],
        }
    def validate_advice(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate advice value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'affirm' or intent == 'deny':
            return {"request": intent}
        else:
            return {"request": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        intent = tracker.get_slot("request")
        if intent == 'affirm'
            return [FollowupAction("health_question_form")]
        elif intent == 'deny':
            dispatcher.utter_message(text="dạ vâng, em cảm ơn chị!")
            return [FollowupAction("action_chat_restart")]
        else:
            return []
class RequestForm(FormAction):
    def name(self) -> Text:
        return "health_question_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["request"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "request": [self.from_text()],
        }
    def validate_name(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate verifyinfor value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'register' or intent == 'advice':
            return {"request": intent}
        else:
            return {"request": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        intent = tracker.get_slot("request")
        if intent == 'register'
            return [FollowupAction("register_form")]
        elif intent == 'advice':
            return [FollowupAction("advice_form")]
        else:
            return []