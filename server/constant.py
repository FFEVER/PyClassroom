# Network Info
PORT = 8888

# Identifier
I_AM_STUDENT_SENDER = "i_am_student_sender"
I_AM_TEACHER_SENDER = "i_am_teacher_sender"
I_AM_STUDENT_RECEIVER = "i_am_student_receiver"
I_AM_TEACHER_RECEIVER = "i_am_teacher_receiver"
SUCCESS = "success"
FAIL = "fail"

# Teacher commands
START_LIVE = "start_live"
END_LIVE = "end_live"
ADD_MATERIAL = "add_material"
REMOVE_MATERIAL = "remove_mat"
KICK_STUDENT = "kick_student"
CLOSE_ROOM = "close_room"

# Server -> Teacher
CREATE_ROOM_SUCCESS = "room_created_successfully"

# Server -> All
STUDENT_LIST_UPDATED = "student_list_updated"
MESSAGE_FROM_STUDENT = "message_from_student"

# Server -> Student
JOIN_ROOM_SUCCESS = "join_room_success"
JOIN_ROOM_FAIL = "join_room_failed"

# Student commands
JOIN_ROOM = "join_room"
LEAVE_ROOM = "leave_room"
SEND_MSG = "send_message"
REFRESH_ROOM_LIST = "refresh_room_list"
REFRESH_MATERIAL = "refresh_material"