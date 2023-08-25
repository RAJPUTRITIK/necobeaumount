from django.shortcuts import render
from .models import Detail

def index(request):
    return render(request, 'index.html')

def entry_data(request):
    if request.method=='POST':
        s=Detail.objects.create(
            building=request.POST['building'],
            floor=request.POST['floornumber'],
            room_number=request.POST['roomnumber'],
            owner_name=request.POST['ownername'],
            member=request.POST['member'],
            mobile_number=request.POST['mobilenumber'],
        )
        return render(request,'index.html',{'msg':'successfully '})
    else:   
        return render(request,'entry_data.html')

def wing(request):
    return render(request, 'wing.html')

def building_a(request):
    floor_a=range(1,11)
    return render(request, 'building_a.html', {'floor_a': floor_a})

def floor_room_a(request,i):
    if i==1:
        rooms= range(101,109)
        return render(request, 'floor_room_a.html',{'rooms':rooms})
    elif i==2:
        rooms= range(201,209)
        return render(request, 'floor_room_a.html',{'rooms':rooms})
    elif i==3:
        rooms= range(301,309)
        return render(request, 'floor_room_a.html',{'rooms':rooms})
    elif i==4:
        rooms= range(401,409)
        return render(request, 'floor_room_a.html',{'rooms':rooms})
    elif i==5:
        rooms= range(501,509)
        return render(request, 'floor_room_a.html',{'rooms':rooms})
    elif i==6:
        rooms= range(601,609)
        return render(request, 'floor_room_a.html',{'rooms':rooms})
    elif i==7:
        rooms= range(701,709)
        return render(request, 'floor_room_a.html',{'rooms':rooms})
    elif i==8:
        rooms= range(801,809)
        return render(request, 'floor_room_a.html',{'rooms':rooms})
    elif i==9:
        rooms= range(901,909)
        return render(request, 'floor_room_a.html',{'rooms':rooms})
    elif i==10:
        rooms= range(1001,1009)
        return render(request, 'floor_room_a.html',{'rooms':rooms})
    else:
        return render(request, 'floor_room_a.html',{'msg':'no data found'})
        

def building_b(request):
    floors_b = range(1, 11)
    return render(request, 'building_b.html', {'floors_b': floors_b})

   
def floor_room_b(request,i):
    if i==1:
        rooms= range(101,109)
        return render(request, 'floor_room_b.html',{'rooms':rooms})
    elif i==2:
        rooms= range(201,209)
        return render(request, 'floor_room_b.html',{'rooms':rooms})
    elif i==3:
        rooms= range(301,309)
        return render(request, 'floor_room_b.html',{'rooms':rooms})
    elif i==4:
        rooms= range(401,409)
        return render(request, 'floor_room_b.html',{'rooms':rooms})
    elif i==5:
        rooms= range(501,509)
        return render(request, 'floor_room_b.html',{'rooms':rooms})
    elif i==6:
        rooms= range(601,609)
        return render(request, 'floor_room_b.html',{'rooms':rooms})
    elif i==7:
        rooms= range(701,709)
        return render(request, 'floor_room_b.html',{'rooms':rooms})
    elif i==8:
        rooms= range(801,809)
        return render(request, 'floor_room_b.html',{'rooms':rooms})
    elif i==9:
        rooms= range(901,909)
        return render(request, 'floor_room_b.html',{'rooms':rooms})
    elif i==10:
        rooms= range(1001,1009)
        return render(request, 'floor_room_b.html',{'rooms':rooms})
    else:
        return render(request, 'floor_room_b.html',{'msg':'no data found'})

def building_a_data(request,room):
    data=Detail.objects.filter(building='A',room_number=room)
   
    return render(request,'building_a_data.html',{'data':data,'room':room})

def building_b_data(request,room):
    data=Detail.objects.filter(building='B',room_number=room)
    return render(request, 'building_b_data.html',{'data':data,'room':room})


def update_building_a_data(request):
    return render(request,'update_building_a_data.html')














