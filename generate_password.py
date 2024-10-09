from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# print(pwd_context.hash('admin'))

print(pwd_context.verify('admin', '$2b$12$UdDiQZ6th3gXDDO0se8fI.bDA5kUmC2/yJIe/lm24AQP6g2e/vBqi'))