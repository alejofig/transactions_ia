Para desplegar la imagen de docker en lambda:
1. Crear la imagen: docker build -t lambda_openai .     
2. tagear la imagen con la info del repo de ECR: docker tag
3. subir la imagen con docker push y la ruta.
4. Desplegar la función con docker apuntando al ECR.