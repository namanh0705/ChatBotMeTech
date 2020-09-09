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

class RequestForm(FormAction):
    def name(self) -> Text:
        return "resquest_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["name"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "name": [self.from_text()],
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
        entity = tracker.latest_message['entities']
        if intent == 'name_customer':
            if not entity:
                return {"name": None}
            else:
                name = entity[0]['value']
                return {"name": name}
        else:
            return {"name": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        return [FollowupAction("id_ticket_form")]
class IdTicketForm(FormAction):
    def name(self) -> Text:
        return "id_ticket_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["id_ticket","fullname","id_agency", "travel"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "id_ticket": [self.from_text()],
            "fullname": [self.from_text()],
            "id_agency": [self.from_text()],
            "travel": [self.from_text()],
        }
    def validate_id_ticket(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate id_ticket value."""
        intent = tracker.latest_message['intent'].get('name')
        entity = tracker.latest_message['entities']
        text = tracker.latest_message['text']
        print(text)
        if intent == 'id_agency' or intent == 'id_ticket':
            number = "".join(re.findall("[0-9]", text))
            if not entity:
                if not number:
                    return {"id_ticket": None}
                else:
                    print(number)
                    return {"id_ticket": number}
            else:
                ticketid = entity[0]['value']
                return {"id_ticket": ticketid}
        else:
            return {"id_ticket": None}
    def validate_fullname(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate fullname value."""
        intent = tracker.latest_message['intent'].get('name')
        entity = tracker.latest_message['entities']
        if intent == 'fullname' or intent == 'ans_changname':
            
            if not entity:
                return {"fullname": None}
            else:
                fullname = entity[0]['value']
                return {"fullname": fullname}
        else:
            return {"fullname": None}
    def validate_id_agency(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate id_agency value."""
        intent = tracker.latest_message['intent'].get('name')
        entity = tracker.latest_message['entities']
        text = tracker.latest_message['text']
        print(text)
        if intent == 'id_agency' or intent == 'id_ticket':
            number = "".join(re.findall("[0-9]", text))
            if not entity:
                if not number:
                    return {"id_agency": None}
                else:
                    print(number)
                    return {"id_agency": number}
            else:
                idagency = entity[0]['value']
                return {"id_agency": idagency}
        else:
            return {"id_agency": None}
    def validate_travel(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate travel value."""
        intent = tracker.latest_message['intent'].get('name')
        entity = tracker.latest_message['entities']
        if intent == 'travel':
            
            if not entity:
                return {"travel": None}
            else:
                travel = entity[0]['value']
                return {"travel": travel}
        else:
            return {"travel": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        return [FollowupAction("question_form")]
class QuestionForm(FormAction):
    def name(self) -> Text:
        return "question_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["question", "changename", "freeeditname"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "question": [self.from_text()],
            "changename": [self.from_text()],
            "freeeditname": [self.from_text()]
        }
    def validate_question(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate question value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'changename':
            return {"question": intent}
        else:
            return {"question": None}
    def validate_changename(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate changename value."""
        intent = tracker.latest_message['intent'].get('name')
        entity = tracker.latest_message['entities']
        if intent == 'fullname' or intent == 'ans_changname':
            
            if not entity:
                return {"changename": None}
            else:
                changname = entity[0]['value']
                return {"changename": changname}
        else:
            return {"changename": None}
    def validate_freeeditname(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate freeeditname value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'affirm':
            return {"freeeditname": intent}
        else:
            return {"freeeditname": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        return [FollowupAction("confirm_form")]
class ConfirmForm(FormAction):
    def name(self) -> Text:
        return "confirm_form"
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["confirm", "confirm2", "confirm3","confirm4"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "confirm": [self.from_text()],
            "confirm2": [self.from_text()],
            "confirm3": [self.from_text()],
            "confirm4": [self.from_text()],
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
        if intent == 'affirm':
            return {"confirm": intent}
        else:
            return {"confirm": None}
    def validate_confirm2(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate confirm2 value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'affirm': 
            return {"confirm2": intent}
        else:
            return {"confirm2": None}
    def validate_confirm3(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate confirm3 value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'affirm':
            return {"confirm3": intent}
        else:
            return {"confirm3": None}
    def validate_confirm4(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate confirm4 value."""
        intent = tracker.latest_message['intent'].get('name')
        if intent == 'deny':
            return {"confirm4": intent}
        else:
            return {"confirm4": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        name = tracker.get_slot("name")
        dispatcher.utter_message(text="Dạ vâng, cần thêm thông tin anh vui lòng liên hệ lại Tổng Đài. Cảm ơn và xin chào anh {0} ạ".format(name))
        return [FollowupAction("action_chat_restart")]
class ActionRestarted(Action):
    """ This is for restarting the chat"""

    def name(self):
        return "action_chat_restart"

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]