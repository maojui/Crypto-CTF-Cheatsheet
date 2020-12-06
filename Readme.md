# Function

### XOR function

```python
xor = lambda a, b: bytes(ai ^ bi for ai, bi in zip(a, b))
```

## Hash

* [Length extension attack (LEA)](https://gist.github.com/maojui/9b078194c43835e2947b39192f0537c1)
* [SHA-1 Collision](https://gist.github.com/maojui/b33420c5b27f250fe94ec7e085ca4c42)

## RSA


### Factorize modular 

#### Tools

[FactorDB](http://factordb.com/)
[Integer factorization calculator](https://www.alpertron.com.ar/ECM.HTM)
[YAFU Docker (Yet Another Factoring Utility)](https://hub.docker.com/r/eyjhb/yafu)

#### Scripts

* [factordb API](./scripts/factorization/factordb.py) - API for getting well-known prime in FactorDB
* [Pollard's rho](./scripts/factorization/pollard.py) - Efficient factor N when (p - 1) is smooth
* [William's p+1](./scripts/factorization/pollard.py)  - Efficient factor N when (p + 1) is smooth
* [Fermat factorization](./scripts/factorization/fermat_factorization.py) - Fermat Factorization : when p, q are close.
* [Factors a number using the Elliptic Curve Method](https://github.com/martingkelly/pyecm/blob/master/pyecm.py) 

### with low exponent

* [Hastad's Broadcast](./scripts/RSA/hastad_broadcast.py) - 
* [Bleichenbacher](http://www.dsi.unive.it/~focardi/RSA-padding-oracle/)

### with huge exponent

* [Boneh and Durfee Attack](https://gist.github.com/maojui/fa9b5dfd37460bfacff65a7e65eaa177)
* [Wiener Attack](https://gist.github.com/maojui/fad0a9a9899de482a66f08ffa7f4d510)

### Others attack

* [Common Modular Attack](./scripts/RSA/fermat_factorization.py)

### Factoring with Partial Information

* [Partial Prime](https://gist.github.com/maojui/8bf7b9d76c52c049286025e8de2ba1a8)
* [Partial Private Key](https://gist.github.com/maojui/bd55d98d310bab770a6a0681078b444e)

## SSL certificate using python

```python
from Crypto.PublicKey import RSA
key = RSA.importKey(open('publickey.pem','r').read())
```

### Converting Using OpenSSL

Source : [stackoverflow](https://stackoverflow.com/questions/13732826/convert-pem-to-crt-and-key)

Below commands allow you to convert certificates and keys to different formats to make them compatible with specific types of servers or software.

* Convert a PEM file to (.der, .crt)

```
openssl x509 -outform der -in certificate.pem -out certificate.der # DER
openssl x509 -outform der -in certificate.pem -out certificate.crt # CRT
openssl pkcs12 -export -out certificate.pfx -inkey privateKey.key -in certificate.crt -certfile CACert.crt # PFX, P12
openssl crl2pkcs7 -nocrl -certfile certificate.cer -out certificate.p7b -certfile CACert.cer # P7B
```

* Convert a DER file (.crt .cer .der) to PEM

```
openssl x509 -inform der -in certificate.crt -out certificate.pem 
openssl x509 -inform der -in certificate.cer -out certificate.pem 
openssl x509 -inform der -in certificate.der -out certificate.pem
```

* Convert a PKCS#12 file (.pfx .p12) containing a private key and certificates to PEM

```
openssl pkcs12 -in keyStore.pfx -out keyStore.pem -nodes
```

## Cryptosystem

* [Paillier](./scripts/cryptosystem/Paillier.py)
* [SchmidtSamoa](./scripts/cryptosystem/SchmidtSamoa.py)
* [OkamotoUchiyama](./scripts/cryptosystem/OkamotoUchiyama.py)

## NTRU

* [NTRU with weak parameters](https://gist.github.com/maojui/0bab62c95979fe0ff7dcd67e55d1d6f4)

## Mathmatics

* [Find nth_roots on modulo p](https://gist.github.com/maojui/61c10d93db220e9c77b20d274969e363)
* [Chinese remainder theorem](./scripts/Mathmathics/crt.py)
