# kuber
minikube start  
minikube addons enable ingress metrics-server
kubectl.exe apply -f  
minikube service front --url  /или/  kubectl.exe get ing для получения ip, чтобы можно было в файл host добавить {ingress address} {hello-paladen.info}
helm install app .\k8s-helm\  
helm test app