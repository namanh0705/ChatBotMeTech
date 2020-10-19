from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet,Form,ReminderScheduled,ActionReverted,UserUtteranceReverted,FollowupAction,AllSlotsReset
from rasa.core.slots import Slot
from rasa.core.policies.memoization import MemoizationPolicy
import datetime
import time
from threading import Timer
import re
import random
class ActionRestarted(Action):
    """ This is for restarting the chat"""

    def name(self):
        return "action_chat_restart"

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]

class Beginform(FormAction):
    def name(self) -> Text:
        return "begin_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["hello"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "hello": [self.from_text()]
        }
    def validate_hello(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate hello value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'affirm':
            return {"hello": intent}
        elif intent == 'deny':
            return {"hello": intent}
        else:
            return {"hello": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        intent = tracker.get_slot("hello")
        if intent == 'affirm':
            return [FollowupAction("please_form")]
        elif intent == 'deny':
            return [FollowupAction("other_city")]
        else:
            pass
        return []

class Pleaseform(FormAction):
    def name(self) -> Text:
        return "please_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["please"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "please": [self.from_text()]
        }
    def validate_please(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate hello value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'affirm':
            return {"please": intent}
        elif intent == 'deny':
            return {"please": intent}
        else:
            return {"please": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        intent = tracker.get_slot("please")
        if intent == 'affirm':
            dispatcher.utter_message(text="Em xin cảm ơn, Trong ngày hôm nay và chỉ dành riêng cho anh/chị khi nhận được cuộc gọi này, dù giá thị trường khoảng 5 triệu đồng, nhưng lần này anh/chị có thể sở hữu gói bảo hiểm sức khỏe của công ty bảo hiểm dầu khí uy tín, sử dụng tại tất cả các bệnh viện trên toàn quốc. Mà giá chỉ có khoảng 1 triệu đồng/năm khoảng 3,000 đồng mỗi ngày thôi")
            return [FollowupAction("step2_form")]
        elif intent == 'deny':
            dispatcher.utter_message(text="Cảm ơn thời gian của anh/chị")
            return [FollowupAction("action_chat_restart")]
        else:
            pass
        return []

class Other_city(FormAction):
    def name(self) -> Text:
        return "other_city"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["othercity", "othercityask"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "othercity": [self.from_text()],
            "othercityask": [self.from_text()]
        }
    def validate_othercity(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate othercity value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'ans_other_city':
            return {"ans_other_city": intent}
        else:
            return {"hello": None}
    def validate_othercityask(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate othercityask value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'affirm':
            return {"othercityask": intent}
        elif intent == 'deny':
            return {"othercityask": intent}
        else:
            return {"othercityask": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        intent = tracker.get_slot("othercityask")
        if intent == 'affirm':
            dispatcher.utter_message(text="Em xin cảm ơn, Trong ngày hôm nay và chỉ dành riêng cho anh/chị khi nhận được cuộc gọi này, dù giá thị trường khoảng 5 triệu đồng, nhưng lần này anh/chị có thể sở hữu gói bảo hiểm sức khỏe của công ty bảo hiểm dầu khí uy tín, sử dụng tại tất cả các bệnh viện trên toàn quốc. Mà giá chỉ có khoảng 1 triệu đồng/năm khoảng 3,000 đồng mỗi ngày thôi")
            return [FollowupAction("step2_form")]
        elif intent == 'deny':
            dispatcher.utter_message(text="Cảm ơn thời gian của anh/chị")
            return [FollowupAction("action_chat_restart")]
        else:
            pass
        return []

class Step2Form(FormAction):
    def name(self) -> Text:
        return "step2_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["advice2"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "advice2": [self.from_text()]
        }
    def validate_advice2(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate advice2 value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'affirm':
            return {"advice2": intent}
        elif intent == 'deny':
            return {"advice2": intent}
        else:
            return {"advice2": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        intent = tracker.get_slot("advice2")
        if intent == 'affirm':
            return [FollowupAction("health1_question_form")]
        elif intent == 'deny':
            dispatcher.utter_message(text="Cảm ơn thời gian của anh/chị")
            return [FollowupAction("action_chat_restart")]
        else:
            pass
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

class ConfirmForm(FormAction):
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
        """Validate confirm value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'choice':
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

