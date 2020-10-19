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
<<<<<<< HEAD
            pass
        return []
=======
            return []
class Healthy1Form(FormAction):
    def name(self) -> Text:
        return "health1_question_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["healthy1"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "healthy1": [self.from_text()],
        }
    def validate_healthy1(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate verifyinfor value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'affirm' or intent == 'deny':
            return {"healthy1": intent}
        else:
            return {"healthy1": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        intent = tracker.get_slot("healthy1")
        if intent == 'affirm':
            return [FollowupAction("detail1_healthy_form")]
        elif intent == 'deny':
            return [FollowupAction("health2_question_form")]
        else:
            return []
class Healthy2Form(FormAction):
    def name(self) -> Text:
        return "health2_question_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["healthy2"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "healthy2": [self.from_text()],
        }
    def validate_healthy2(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate verifyinfor value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'affirm' or intent == 'deny':
            return {"healthy2": intent}
        else:
            return {"healthy2": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        intent = tracker.get_slot("healthy2")
        if intent == 'affirm':
            return [FollowupAction("detail2_healthy_form")]
        elif intent == 'deny':
            return [FollowupAction("health3_question_form")]
        else:
            return []
class Healthy3Form(FormAction):
    def name(self) -> Text:
        return "health3_question_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["healthy3"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "healthy3": [self.from_text()],
        }
    def validate_healthy3(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate verifyinfor value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'affirm' or intent == 'deny':
            return {"healthy3": intent}
        else:
            return {"healthy3": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        intent = tracker.get_slot("healthy3")
        if intent == 'affirm':
            return [FollowupAction("detail3_healthy_form")]
        elif intent == 'deny':
            return [FollowupAction("health4_question_form")]
        else:
            return []
class Healthy4Form(FormAction):
    def name(self) -> Text:
        return "health4_question_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["healthy4"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "healthy4": [self.from_text()],
        }
    def validate_healthy(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate verifyinfor value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'affirm' or intent == 'deny':
            return {"healthy4": intent}
        else:
            return {"healthy4": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        return [FollowupAction("confirm_form")]
class Detail1HealthyForm(FormAction):
    def name(self) -> Text:
        return "detail1_healthy_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["detail1"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "detail1": [self.from_text()],
        }  
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        return [FollowupAction("health2_question_form")]
class Detail2HealthyForm(FormAction):
    def name(self) -> Text:
        return "detail2_healthy_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["detail2"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "detail2": [self.from_text()],
        }  
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        return [FollowupAction("health3_question_form")]
class Detail3HealthyForm(FormAction):
    def name(self) -> Text:
        return "detail3_healthy_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["detail3"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "detail3": [self.from_text()],
        }  
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        return [FollowupAction("health4_question_form")]
>>>>>>> 655df688c1760c970cbbaca4253138ffcfe2a3b6
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