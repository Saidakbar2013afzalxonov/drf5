from django.shortcuts import render
from .models import Students
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
# class StudentView(viewsets.ModelViewSet):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer



@api_view(['GET'])
def StudentList(request):
    students = Students.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def StudentView(request, pk):
    student = Students.objects.get(pk=pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)


@api_view(['POST'])
def StudentCreate(request):
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(
        {"message": "Ma'lumotlar noto'g'ri kiritildi!"},
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['PUT', 'PATCH'])
def StudentUpdate(request, pk):
    student = Students.objects.get(pk=pk)

    serializer = StudentSerializer(student, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(
        {"message": "Talabani yangilashda xatolik yuz berdi!"},
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['DELETE'])
def StudentDelete(request, pk):
    student = Students.objects.get(pk=pk)
    student.delete()

    return Response(
        {"message": "Talaba o'chirildi!"},
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['GET', 'POST'])
def StudentListCreate(request):
    if request.method == 'GET':
        students = Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            {"message": "Ma'lumotlar noto'g'ri kiritildi!"},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def StudentDetail(request, pk):
    student = Students.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            {"message": "Talabani to'liq yangilashda xatolik yuz berdi!"},
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'PATCH':
        serializer = StudentSerializer(student, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            {"message": "Talabani qisman yangilashda xatolik yuz berdi!"},
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':
        student.delete()
        return Response(
            {"message": "Talaba muvaffaqiyatli o'chirildi!"},
            status=status.HTTP_204_NO_CONTENT
        )