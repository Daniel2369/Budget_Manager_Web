
# Project Title

DevOps 2025 Technion course - Docker&Apache2 Project.



## 🚀 About Me
I'm a T3 technical support engineer in Paloalto networks.

You are welcome to connect with me on Linkedin:
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/daniel-berliant-6725241a9/)


## Authors

- [@Daniel2369](https://github.com/Daniel2369)


## Documentation

[Documentation: Self signed certificate](https://medium.com/@pasanglamatamang/configuring-a-self-signed-ssl-certificate-on-a-apache-server-cbcd6eefdf1a)

[Documentation: User basic auth](https://www.digitalocean.com/community/tutorials/how-to-set-up-password-authentication-with-apache-on-ubuntu-14-04)




## Features

- **User Authentication** – Secure login and registration.
- **Add/Remove Transactions** – Track your income and expenses easily.
- **Self-signed certificate** - ADD SSL Layer
- **View Transactions history** - Track your Transactions history.




## Installation

Install my-project with docker

```bash
  1. Pull the docker image: 
  https://hub.docker.com/repository/docker/beri1/apache2/general
  2. Create a running container with an open port to the host:
  docker run -d --it -p 8282:443 bash
  3. Edit /etc/hosts file in host with the host IP and the domain name my_balance
  4. Access in the hosts's browser to: https://my_balance:8282
  5. User: Daniel Pass: 1234
```
