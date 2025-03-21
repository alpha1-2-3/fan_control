from django.shortcuts import render  # Import this
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import socket
import json

MATLAB_IP = "127.0.0.1"  # MATLAB's TCP Server
MATLAB_PORT = 5001  # Port MATLAB will listen on

@csrf_exempt  # Disable CSRF for testing
def set_speed(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Read JSON data
            print("Received Data:", data)  # Debugging line
            
            speed = data.get("speed")
            if not speed:
                return JsonResponse({"error": "Speed value missing"}, status=400)
            
            # Send data to MATLAB TCP Server
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((MATLAB_IP, MATLAB_PORT))
                s.sendall(speed.encode())

            return JsonResponse({"status": "success", "selected_speed": speed})

        except Exception as e:
            print("Error:", str(e))  # Debugging line
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)



def home(request):
    return render(request, 'index.html')  # Render the homepage
