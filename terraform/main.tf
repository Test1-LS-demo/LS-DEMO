# Vulnerable Terraform configuration
resource "aws_s3_bucket" "example" {
  bucket = "my-vulnerable-bucket"
  
  # Vulnerability: Public read access
  acl = "public-read"
}

resource "aws_security_group" "web" {
  name = "web-sg"
  
  # Vulnerability: Open to all traffic
  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"
  
  # Vulnerability: No encryption
  root_block_device {
    encrypted = false
  }
  
  # Vulnerability: Hardcoded credentials
  user_data = <<-EOF
    #!/bin/bash
    echo "admin:password123" | chpasswd
  EOF
}
