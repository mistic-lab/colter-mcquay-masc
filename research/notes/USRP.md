## Getting USRP's Setup

- change nic to manual ip address of `192.168.10.1`
- run `uhd_find_devices` to make sure the USRP is available
- run `uhd_usrp_probe`
- Update the firmware via:

```sh
 "/usr/lib/uhd/utils/uhd_images_downloader.py"
 "/usr/bin/uhd_image_loader" \
    --args="type=usrp2,addr=192.168.10.2"
```

> You must unplug the USRP before the firmware will take effect


### Changing IP Address

- Get serial number from `uhd_find_devices`

```sh
/usr/lib/uhd/utils$ ./usrp_burn_mb_eeprom --args="serial=E0R13WCUP" --values="ip-addr=192.168.10.3"
```

## E310

[E310 Docs](https://kb.ettus.com/E310/E312_Getting_Started_Guides)

