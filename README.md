# kuber
minikube start
minikube addons enable ingress
kubectl.exe apply -f
minikube service front --url   или   kubectl.exe get ing для получения ip, чтобы можно было в файл host добавить ip <ingress address> <hello-paladen.info>
