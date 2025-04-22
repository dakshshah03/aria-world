NAME=daksh-asl-desktop # Change this to your initials
POD_NAME=daksh-autoslug # Change this to your initials
CACHE_NAME=desktop-cache # Change this to your initials
SERVICE_NAME=kubectl.exe

if [ "$1" -eq 1 ]; then
    $SERVICE_NAME delete deployment $NAME
    $SERVICE_NAME delete service $NAME
    $SERVICE_NAME delete ingress $NAME
elif [ "$1" -eq 0 ]; then
    # kubectl create -f storage.yml
    $SERVICE_NAME create -f cache.yml
    $SERVICE_NAME create -f desktop.yml
    $SERVICE_NAME create -f desktop-ingress.yml
# elif [ "$1" -eq 2 ]; then
#     kubectl delete deployment $NAME
#     kubectl delete service $NAME
#     kubectl delete ingress $NAME
#     kubectl delete pvc --now $POD_NAME
#     kubectl delete pvc --now $CACHE_NAME
else
    echo "Usage: $0 [1]"
    exit 1
fi