FROM quay.io/maroonayoub/i4q-restapi:pybase

ARG modelpath

# copy py app files
RUN chown -R 1000790000:0 /app
RUN chmod -R 755 /app

ENV TORCH_HOME /app

WORKDIR /app
ADD rest-api /app

# copy ML model
COPY ${modelpath} /app/yolo.pt

EXPOSE 6000

USER 1000790000
CMD ["python", "restapi.py", "--port=6000", "--model=yolo.pt"]