def createNote(request):
    data = request.data
    note = Note.objects.create(body=data['body'])
    serializer = NoteSerializer(data=data, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)