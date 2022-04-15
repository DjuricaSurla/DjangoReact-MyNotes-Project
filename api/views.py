from rest_framework.response import Response # Response from Rest Framework, sends back the response in the form of an object
from rest_framework.decorators import api_view # Api view decorator 
from .utils import updateNote, getNoteDetail, deleteNote, getAllNotes, createNote


# Create your views here.

@api_view(['GET']) # We use this to change our website appearance to api view, we can put methods we want in here
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def getNotes(request):
    if request.method == 'GET':
        return getAllNotes(request)

    if request.method == 'POST':
        return createNote(request)


@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):

    if request.method == 'GET':
        return getNoteDetail(request, pk)

    if request.method == 'PUT':
        return updateNote(request, pk)

    if request.method == 'DELETE':
        return deleteNote(request, pk)

    











# api_view(['GET'])
# def getNotes(request):
#     notes = Note.objects.all().order_by('-updated') # Getting all objects from notes model
#     serializer = NoteSerializer(notes, many=True) # We need to serialize the data (Convert it to format we can read) - many=true means do this serialization for all objects
#     return Response(serializer.data) 

# api_view(['GET'])
# def getNote(request, pk):
#     note = Note.objects.get(id=pk) 
#     serializer = NoteSerializer(note, many=False) # We serialize only one object
#     return Response(serializer.data)


# @api_view(['POST'])
# def createNote(request):
#     data = request.data
#     note = Note.objects.create(
#         body = data['body']
#     )
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)


# @api_view(['PUT'])
# def updateNote(request, pk):
#     data = request.data
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(instance=note, data=data) # Here we update the note with the new data we get from the frontend.

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

# @api_view(['DELETE'])
# def deleteNote(request, pk):
#     note = Note.objects.get(id=pk)
#     note.delete()
#     return Response('Note was deleted!')
    