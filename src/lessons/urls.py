from django.urls import path, re_path
from lessons.livestream import (
    index,
    livestreams,
    newLS,
    deleteStream,
    getStream,
    editStream
)


from lessons.views import (
    lessons,
    getLessons,
    getQuestions,
    addResource,
    video_watched,
    vid,
    getTest,
    pdf_read,
    deleteMedia,
    studentStats,
    lessonComments,
    likeComment,
    deleteComment,
    getComment,
    updateComment,
    newCount,
    pdfView,
    lessonPdfComments,
    getPdfComment,
    updatePdfComment,
    deletePdfComment,
    likePdfComment
)

app_name = 'lessons'

urlpatterns = [
    # Livestream path
    path('livestream', index, name='livestream'),
    path('get-livestream', livestreams, name='livestreams'),
    path('new-livestream', newLS, name='new-LS'),
    path('delete-stream', deleteStream, name='delete-stream'),
    path('get-stream', getStream, name='get-stream'),
    path('update-stream', editStream, name='edit-stream'),

    # Lessons path
    re_path(r'^lesson-pdf-comments$', lessonPdfComments, name='pdfcomments'),
    re_path(r'^lesson-comments$', lessonComments, name='comments'),
    path('get-lesson-pdf-comment', getPdfComment, name='getPdfComment'),
    path('get-lesson-comment', getComment, name='getComment'),
    path('new-lesson-asset', newCount, name='newCount'),
    path('update-lesson-pdf-comment', updatePdfComment, name='updatePdfComment'),
    path('update-lesson-comment', updateComment, name='updateComment'),
    path('delete-lesson-pdf-comment', deletePdfComment, name='deletePdfComment'),
    path('delete-lesson-comment', deleteComment, name='deleteComment'),
    path('like-lesson-pdf-comment', likePdfComment, name='likePdf'),
    path('like-lesson-comment', likeComment, name='like'),
    path('delete-lesson-media', deleteMedia, name='delete-media'),
    path('lessons', lessons, name='lessons'),
    path('get-lessons', getLessons, name='get_lessons'),
    path('get-questions', getQuestions, name='get-questions'),
    path('add-lesson-resource', addResource, name='add-lesson-resource'),
    path('video-mark-watched', video_watched, name='mark_watched'),
    path('lesson/pdf/<int:id>', pdfView, name='pdf'),
    path('lesson/video/<int:id>', vid, name='video'),
    path('lesson/test/<int:id>', getTest, name='Test'),
    path('mark-lesson-pdf-read', pdf_read, name='mark_read'),
    re_path(r'^lesson-student-stats$', studentStats, name='student-stats'),
]
