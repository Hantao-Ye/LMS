from django.urls import re_path

from . import views

# Import custom views.
from apps.teacher.views import announcement
from apps.teacher.views import syllabus
from apps.teacher.views import policy
from apps.teacher.views import lecture
from apps.teacher.views import lecture_note
from apps.teacher.views import assignment
from apps.teacher.views import quiz
from apps.teacher.views import exam
from apps.teacher.views import overview
from apps.teacher.views import discussion
from apps.teacher.views import peer_review
from apps.teacher.views import setting

urlpatterns = [
    # Syllabus
    re_path(r'^teacher/course/(\d+)/overview$', overview.overview_page),
    re_path(r'^teacher/course/(\d+)/submit_course_for_review$', overview.submit_course_for_review),

    # Announcement
    re_path(r'^teacher/course/(\d+)/$', announcement.announcements_page),
    re_path(r'^teacher/course/(\d+)/home$', announcement.announcements_page),
    re_path(r'^teacher/course/(\d+)/announcement$', announcement.announcements_page),
    re_path(r'^teacher/course/(\d+)/announcements_table$', announcement.announcements_table),
    re_path(r'^teacher/course/(\d+)/announcement_modal$', announcement.announcement_modal),
    re_path(r'^teacher/course/(\d+)/save_announcement$', announcement.save_announcement),
    re_path(r'^teacher/course/(\d+)/delete_announcement$', announcement.delete_announcement),

    # Syllabus
    re_path(r'^teacher/course/(\d+)/syllabus$', syllabus.syllabus_page),
    re_path(r'^teacher/course/(\d+)/syllabus_modal$', syllabus.syllabus_modal),
    re_path(r'^teacher/course/(\d+)/save_syllabus$', syllabus.save_syllabus),
    re_path(r'^teacher/course/(\d+)/delete_syllabus$', syllabus.delete_syllabus),

    # Policy
    re_path(r'^teacher/course/(\d+)/policy$', policy.policy_page),
    re_path(r'^teacher/course/(\d+)/policy_modal$', policy.policy_modal),
    re_path(r'^teacher/course/(\d+)/save_policy$', policy.save_policy),
    re_path(r'^teacher/course/(\d+)/delete_policy$', policy.delete_policy),

    # Lecture
    re_path(r'^teacher/course/(\d+)/lectures$', lecture.lectures_page),
    re_path(r'^teacher/course/(\d+)/lectures_table$', lecture.lectures_table),
    re_path(r'^teacher/course/(\d+)/lecture_modal$', lecture.lecture_modal),
    re_path(r'^teacher/course/(\d+)/save_lecture$', lecture.save_lecture),
    re_path(r'^teacher/course/(\d+)/delete_lecture$', lecture.delete_lecture),

    # Lecture Note(s)
    re_path(r'^teacher/course/(\d+)/lecture/(\d+)/notes$', lecture_note.lecture_notes_page),
    re_path(r'^teacher/course/(\d+)/lecture/(\d+)/lecture_notes_table$', lecture_note.lecture_notes_table),
    re_path(r'^teacher/course/(\d+)/lecture/(\d+)/lecture_note_modal$', lecture_note.lecture_note_modal),
    re_path(r'^teacher/course/(\d+)/lecture/(\d+)/save_lecture_note$', lecture_note.save_lecture_note),
    re_path(r'^teacher/course/(\d+)/lecture/(\d+)/delete_lecture_note$', lecture_note.delete_lecture_note),
                       
    # Assignment(s)
    re_path(r'^teacher/course/(\d+)/assignments$', assignment.assignments_page),
    re_path(r'^teacher/course/(\d+)/assignments_table$', assignment.assignments_table),
    re_path(r'^teacher/course/(\d+)/assignment_modal$', assignment.assignment_modal),
    re_path(r'^teacher/course/(\d+)/save_assignment$', assignment.save_assignment),
    re_path(r'^teacher/course/(\d+)/delete_assignment$', assignment.delete_assignment),

    # Assignment
    re_path(r'^teacher/course/(\d+)/assignment/(\d+)$', assignment.assignment_page),
    re_path(r'^teacher/course/(\d+)/assignment/(\d+)/questions_table$', assignment.questions_table),
    re_path(r'^teacher/course/(\d+)/assignment/(\d+)/question_type_modal$', assignment.question_type_modal),
    re_path(r'^teacher/course/(\d+)/assignment/(\d+)/question_essay_modal$', assignment.question_essay_modal),
    re_path(r'^teacher/course/(\d+)/assignment/(\d+)/question_multiple_choice_modal$', assignment.question_multiple_choice_modal),
    re_path(r'^teacher/course/(\d+)/assignment/(\d+)/question_true_false_modal$', assignment.question_true_false_modal),
    re_path(r'^teacher/course/(\d+)/assignment/(\d+)/question_response_modal$', assignment.question_response_modal),
    re_path(r'^teacher/course/(\d+)/assignment/(\d+)/save_question$', assignment.save_question),
    re_path(r'^teacher/course/(\d+)/assignment/(\d+)/delete_question$', assignment.delete_question),

    # Quiz(es)
    re_path(r'^teacher/course/(\d+)/quizzes$', quiz.quizzes_page),
    re_path(r'^teacher/course/(\d+)/quizzes_table$', quiz.quizzes_table),
    re_path(r'^teacher/course/(\d+)/quiz_modal$', quiz.quiz_modal),
    re_path(r'^teacher/course/(\d+)/save_quiz$', quiz.save_quiz),
    re_path(r'^teacher/course/(\d+)/delete_quiz$', quiz.delete_quiz),

    # Quiz
    re_path(r'^teacher/course/(\d+)/quiz/(\d+)$', quiz.quiz_page),
    re_path(r'^teacher/course/(\d+)/quiz/(\d+)/questions_table$', quiz.questions_table),
    re_path(r'^teacher/course/(\d+)/quiz/(\d+)/question_type_modal$', quiz.question_type_modal),
    re_path(r'^teacher/course/(\d+)/quiz/(\d+)/question_true_false_modal$', quiz.question_true_false_modal),
    re_path(r'^teacher/course/(\d+)/quiz/(\d+)/save_question$', quiz.save_question),
    re_path(r'^teacher/course/(\d+)/quiz/(\d+)/delete_question$', quiz.delete_question),

    # Exam(s)
    re_path(r'^teacher/course/(\d+)/exams$', exam.exams_page),
    re_path(r'^teacher/course/(\d+)/exams_table$', exam.exams_table),
    re_path(r'^teacher/course/(\d+)/exam_modal$', exam.exam_modal),
    re_path(r'^teacher/course/(\d+)/save_exam$', exam.save_exam),
    re_path(r'^teacher/course/(\d+)/delete_exam$', exam.delete_exam),
    
    # # Exam
    re_path(r'^teacher/course/(\d+)/exam/(\d+)$', exam.exam_page),
    re_path(r'^teacher/course/(\d+)/exam/(\d+)/questions_table$', exam.questions_table),
    re_path(r'^teacher/course/(\d+)/exam/(\d+)/question_type_modal$', exam.question_type_modal),
    re_path(r'^teacher/course/(\d+)/exam/(\d+)/question_multiple_choice_modal$', exam.question_multiple_choice_modal),
    re_path(r'^teacher/course/(\d+)/exam/(\d+)/save_question$', exam.save_question),
    re_path(r'^teacher/course/(\d+)/exam/(\d+)/delete_question$', exam.delete_question),
                       
    # Discussion
    re_path(r'^teacher/course/(\d+)/discussion$', discussion.discussion_page),
    re_path(r'^teacher/course/(\d+)/discussions_table$', discussion.discussions_table),
    re_path(r'^teacher/course/(\d+)/new_thread$', discussion.new_thread_modal),
    re_path(r'^teacher/course/(\d+)/insert_thread$', discussion.insert_thread),
    re_path(r'^teacher/course/(\d+)/delete_thread$', discussion.delete_thread),
    re_path(r'^teacher/course/(\d+)/thread/(\d+)$', discussion.posts_page),
    re_path(r'^teacher/course/(\d+)/thread/(\d+)/posts_table$', discussion.posts_table),
    re_path(r'^teacher/course/(\d+)/thread/(\d+)/new_post$', discussion.new_post_modal),
    re_path(r'^teacher/course/(\d+)/thread/(\d+)/insert_post$', discussion.insert_post),
                       
    # Peer-Review
    re_path(r'^teacher/course/(\d+)/peer_reviews$', peer_review.peer_reviews_page),
    re_path(r'^teacher/course/(\d+)/peer_review/(\d+)$', peer_review.assignment_page),
    re_path(r'^teacher/course/(\d+)/peer_review/(\d+)/peer_review_modal$', peer_review.peer_review_modal),
    re_path(r'^teacher/course/(\d+)/peer_review/(\d+)/save_peer_review$', peer_review.save_peer_review),
    re_path(r'^teacher/course/(\d+)/peer_review/(\d+)/delete_peer_review$', peer_review.delete_peer_review),
    re_path(r'^teacher/course/(\d+)/peer_review/(\d+)/update_assignment_marks$', peer_review.update_assignment_marks),
                       
    # Settings
    re_path(r'^teacher/course/(\d+)/settings$', setting.settings_page),
    re_path(r'^teacher/course/(\d+)/suspend_course$', setting.suspend_course),
]
