## Logar no Graylog como Admin

A senha do usuário `admin` precisa ser fornecida no formato de uma hash SHA256. Você pode gerá-la manualmente com: 

```bash
echo -n senhadoadmin | shasum -a 256
```

```hash
fec576ecc231a923f56df2b8695df21087324a951fc1beff2af9a42d3bb6f9d1
```

Adicione a HASH a váriávle de ambiente `GRAYLOG_ROOT_PASSWORD_SHA2` no `docker-compose.yml`
