resource "aws_instance" "web" {
  ami                    = "ami-008bcc0a51a849165" #ubuntu 20
  instance_type          = "t3.micro"
  key_name               = "react-ec2-key"
  vpc_security_group_ids = [aws_security_group.security_group_react.id]

  tags = {
    Name = "react-app-ec2" #give your ec2 name here
  }
}
