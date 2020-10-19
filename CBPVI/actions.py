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

class IdAskForm(FormAction):
    def name(self) -> Text:
        return "id_ask_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["id","confirmid"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "id": [self.from_text()],
            "confirmid": [self.from_text()]
        }
    def validate_id(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate id value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'id_customer':
            entity = tracker.latest_message['entities']
            if not entity:
                return {"id": None}
            else:
                name = entity[0]['value']
                name = name.replace(" ","")
                return {"id": name}
        else:
            return {"id": None}
    def validate_confirmid(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate confirmid value."""
        intent = tracker.latest_message['intent'].get('name')
        confidence = tracker.latest_message['intent'].get('confidence')
        if intent == 'affirm' and confidence >= 0.6:
            return {"confirmid": intent }
        elif intent == 'deny' and confidence >= 0.6:
            return {"confirmid": intent }
        else:
            return {"confirmid": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        confirm = tracker.get_slot("confirmid")
        if confirm == 'affirm':
            return [FollowupAction("confirm_form")]
        elif confirm == 'deny':
            return [SlotSet("id", None),SlotSet("confirmid", None), FollowupAction("id_ask_form")]
        else:
            pass
        return []
class Confirm(FormAction):
    def name(self) -> Text:
        return "confirm_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["confirm"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "confirm": [self.from_text()],
        }
    def validate_confirm(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate verifyinfor value."""
        intent = tracker.latest_message['intent'].get('name')
        confidence = tracker.latest_message['intent'].get('confidence')
        if intent == 'affirm' and confidence >= 0.6:
            return {"confirm": intent }
        elif intent == 'deny' and confidence >= 0.6:
            return {"confirm": intent }
        else:
            return {"confirm": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        id = tracker.get_slot("confirm")
        if id == 'affirm':
            dispatcher.utter_message(text="2|Chúc mừng quý khách đã nhận được phần quà")
        elif id == 'deny':
            dispatcher.utter_message(text="3|Quý khách vui lòng cho biết mã số định danh")
        else:
            pass
        return [FollowupAction("action_chat_restart")]

class ActionRestarted(Action):
    """ This is for restarting the chat"""

    def name(self):
        return "action_chat_restart"

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]