# Copyright IBM Corp All Rights Reserved.
# Copyright London Stock Exchange Group All Rights Reserved.
#
# SPDX-License-Identifier: Apache-2.0
#
# -------------------------------------------------------------
# This makefile defines the following targets
#
#   - all (default) - formats the code, runs liners, downloads vendor libs, and builds executable
#   - fmt - formats the code
#   - vendor - download all third party libraries and puts them inside vendor directory
#   - clean-vendor - removes third party libraries from vendor directory
#   - build - builds the controller
#   - build-images - builds docker image locally for running the components using docker
#   - push-images - pushes the local docker image to docker registry
#   - clean - cleans the build directories
#   - clean-all - superset of 'clean' that also removes vendor dir
#   - lint - runs code analysis tools

IMAGE_TAG ?= latest

.PHONY: docker-build-restapi			##builds docker image locally for restapi component
docker-build-restapi:
	docker build -f rest-api/Dockerfile -t quay.io/maroonayoub/i4q-restapi:${IMAGE_TAG} --build-arg modelpath=${MODELPATH} .

.PHONY: docker-build-webapp			##builds docker image locally for webapp component
docker-build-webapp:
	docker build -f webapp/Dockerfile -t quay.io/maroonayoub/i4q-webapp:${IMAGE_TAG} --build-arg restapi=${RESTAPI} .

.PHONY: docker-push-restapi			##pushes the local docker image to docker registry
docker-push-restapi: docker-build-restapi
	@docker push quay.io/maroonayoub/i4q-restapi:${IMAGE_TAG}

.PHONY: docker-push-webapp			##pushes the local docker image to docker registry
docker-push-webapp: docker-build-webapp
	@docker push quay.io/maroonayoub/i4q-webapp:${IMAGE_TAG}