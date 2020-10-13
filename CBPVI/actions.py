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
        if intent == 'register':
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
            return {"advice": intent}
        else:
            return {"advice": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        intent = tracker.get_slot("advice")
        if intent == 'affirm':
            return [FollowupAction("health1_question_form")]
        elif intent == 'deny':
            dispatcher.utter_message(text="dạ vâng, em cảm ơn chị!")
            return [FollowupAction("action_chat_restart")]
        else:
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
        if intent == 'copper' or intent == 'silver' or intent == 'gold' or intent == 'diamon':
            return {"confirm": intent}
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
        intent = tracker.get_slot("healthy4")
        if intent == 'affirm':
            return [FollowupAction("register_form")]
        elif intent == 'deny':
            return [FollowupAction("advice_form")]
        else:
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
        if intent == 'copper' or intent == 'silver' or intent == 'gold' or intent == 'diamon':
            return {"confirm": intent}
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
        return [FollowupAction("infor_form")]
class InforForm(FormAction):
    def name(self) -> Text:
        return "infor_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["fullname","humanid","birthday"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "fullname": [self.from_text()],
            "humanid": [self.from_text()],
            "birthday": [self.from_text()]
        }
    def validate_fullname(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate fullname value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'fullname':
            return {"fullname": intent}
        else:
            return {"fullname": None}
    def validate_humanid(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate verifyinfor value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'humanid':
            return {"humanid": intent}
        else:
            return {"humanid": None}
    def validate_birthday(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate birthday value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'birthday':
            return {"birthday": intent}
        else:
            return {"birthday": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        dispatcher.utter_message(text="Cảm ơn anh/chị")
        return []
