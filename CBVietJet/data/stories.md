## happy path
* greet
    - utter_greet
* request
    - resquest_form
    - form{"name":"resquest_form"}
    - slot{"requested_slot":"name"}
* name_customer{"name":"Nam"}
    - resquest_form
    - form{"name":null}
    - slot{"name":"Nam"}
    - id_ticket_form
    - form{"name":"id_ticket_form"}
    - slot{"requested_slot":"id_ticket"}
* id_agency{"idticket":"1231"}
    - id_ticket_form
    - slot{"id_ticket":"1231"}
* ans_changname{"fullname":"Nguyễn Nam Anh"}
    - id_ticket_form
    - slot{"fullname":"Nguyễn Nam Anh"}
* id_agency{"idticket":"23145"}
    - id_ticket_form
    - slot{"id_agency":"23145"}
* travel{"travel":"hà nội hải phòng"}
    - id_ticket_form
    - form{"name":null}
    - slot{"travel":"hà nội hải phòng"}
    - question_form
    - form{"name":"question_form"}
    - slot{"requested_slot":"question"}
* changename
    - question_form
    - slot{"question":"changename"}
* ans_changname{"fullname":"Cao Huy Văn"}
    - question_form
    - slot{"changename":"Cao Huy Văn"}
* affirm
    - question_form
    - form{"name":null}
    - slot{"freeeditname":"affirm"}
    - confirm_form
    - form{"name":"confirm_form"}
    - slot{"requested_slot":"confirm"}
* affirm
    - confirm_form
    - slot{"confirm":"affirm"}
* affirm
    - confirm_form
    - slot{"confirm2":"affirm"}
* affirm
    - confirm_form
    - slot{"confirm3":"affirm"}
* deny
    - confirm_form
    - form{"name":null}
    - slot{"confirm4":"deny"}
    - action_chat_restart
## unhappy path
* greet
    - utter_greet
* request
    - resquest_form
    - form{"name":"resquest_form"}
    - slot{"requested_slot":"name"}
* name_customer{"name":"Văn"}
    - resquest_form
    - form{"name":null}
    - slot{"name":"Văn"}
    - id_ticket_form
    - form{"name":"id_ticket_form"}
    - slot{"requested_slot":"id_ticket"}
* id_agency
    - id_ticket_form
    - slot{"id_ticket":"2456"}
* fullname{"fullname":"Cao Huy Văn"}
    - id_ticket_form
    - slot{"fullname":"Cao Huy Văn"}
* id_agency
    - id_ticket_form
    - slot{"id_agency":null}
* id_agency
    - id_ticket_form
    - slot{"id_agency":"2457156"}
* travel{"travel":"hà nội hải phòng"}
    - id_ticket_form
    - form{"name":null}
    - slot{"travel":"hà nội hải phòng"}
    - question_form
    - form{"name":"question_form"}
    - slot{"requested_slot":"question"}
* changename
    - question_form
    - slot{"question":"changename"}
* ans_changname{"fullname":"Nguyễn Nam Anh"}
    - question_form
    - slot{"changename":"Nguyễn Nam Anh"}
* affirm
    - question_form
    - slot{"freeeditname":"affirm"}
    - confirm_form
    - form{"name":"confirm_form"}
    - slot{"requested_slot":"confirm"}
* affirm
    - confirm_form
    - slot{"confirm":"affirm"}
* affirm
    - confirm_form
    - slot{"confirm2":"affirm"}
* affirm
    - confirm_form
    - slot{"confirm3":"affirm"}
* deny
    - confirm_form
    - form{"name":null}
    - slot{"confirm4":"deny"}
    - action_chat_restart
