from django.shortcuts import render, redirect, get_object_or_404
from .models import Announcement
from .forms import AnnouncementForm

def announcement_list(request):
    announcements = Announcement.objects.all()
    return render(request, 'announcement_list.html', {'announcements': announcements})

def announcement_create(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('announcement_list')
    else:
        form = AnnouncementForm()
    return render(request, 'announcement_create.html', {'form': form})

def announcement_update(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('announcement_list')
    else:
        form = AnnouncementForm(instance=announcement)
    return render(request, 'announcement_update.html', {'form': form})

def announcement_delete(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        announcement.delete()
        return redirect('announcement_list')
    return render(request, 'announcement_delete.html', {'announcement': announcement})
