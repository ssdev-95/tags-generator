# barcode-generator

  A app that automates tags generation for logistic services.

  Using flask to develop a easy to use and scalable application that can generate both barcode and qrcode for logistic services to use.

## Techs

  - Python3 (as main language)
  - Flask (as framework for api)
  - Cerberus (for request validation)

## Tools

  - Neovim
  - Python-pip
  - Python-venv
  - Docker

## Running locally

> Ensure you have Docker installed on selected machine

  Befpre running application, create a file called ` .env ` (or ` .env.test ` if running tests), at the root of project folder.
  With everything set up, run: ` docker-compose --profile [PROFILE] {up|down} [OPTIONS] `

> PROFILE CAN BE:
>   -   'dev'   - for devwçelopment purposes
>   -   'test'  - for twsting purposes
>   -   'prod'  - for deployment purposes
>
>
> `{up|down}` option can start or stop the container, respectively ..
>
>
> OPTIONS can be any available.in docker documentation, such as ` -d `(for running commands alongside the started application), ` --rmi all `(fpr removing docker image after stoping/deleting container), etc ..

## Roadmap

  - [x] an user can generate tags
  - [x] an user can select between QrCode and Barcode to generate a tag
  - [x] a tag can be generated in various formats
  - [x] generated tags can be saved
  - [x] unit tests
  - [x] containerization with docker
  - [ ] send generated tag images to a CDN/Cloud
  - [ ] develop a frontend to consume this api and make it easier for users on browser
  - [ ] add authentication
  - [ ] users can see actual generated tags
  - [ ] deploy

