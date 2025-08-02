#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pybitnuvem

 - File: pybitnuvem/core.py
 - Author: Havocesp <https://github.com/havocesp/pybitnuvem>
 - Created: 2023-01-17
 -
"""
import hashlib
import hmac
import time

import requests

from pybitnuvem.constants import API_PRIVATE_URL


class Bitnuvem:
    """Bitnuvem API wrapper."""

    def __init__(self, apikey: str, secret: str):
        self.apikey = apikey
        self.secret = secret

    def _signature(self, msg: str) -> str:
        return hmac.HMAC(self.secret.encode(), msg.encode(), hashlib.sha256).hexdigest()

    def _request(self, end_point, method=None, **params):
        ts = f'{time.time():.0f}'
        params = dict(timestamp=ts, **params)
        msg = '&'.join(f'{k}={v}' for k, v in params.items() if v and k[0] != '_' and k not in ('self',))

        post_params = dict(api_key=self.apikey, request_body=msg, signature=self._signature(msg))

        response = requests.request(method or 'post', url=f'{API_PRIVATE_URL}/{end_point}', data=post_params, timeout=60)

        if response.ok:
            return response.json()
        else:
            response.raise_for_status()

    def get_balance(self):
        """

        :return:
        """
        return self._request('balance')

    def get_account_bank_list(self):
        """

        :return:
        """
        return self._request('account_bank_list')

    def send(self, amount, address, priority=None):
        """Send BTC to a supplied address.

        :param amount: BTC amount to be send.
        :param address: receiver BTC address.
        :param priority: accepted values: low, regular, high (default: high)
        :return:
        """
        params = dict(amount=amount, address=address, type=priority or 'high')
        return self._request('send', method='post', **params)

    def withdraw(self):
        """

        """
        raise NotImplementedError()

    def order_get(self):
        """

        """
        raise NotImplementedError()

    def order_list(self):
        """

        """
        raise NotImplementedError()

    def order_new(self):
        """

        """
        raise NotImplementedError()

    def order_cancel(self, order_id=None):
        """

        :param order_id:
        :return:
        """
        if order_id:
            return self._request('order_cancel', method='post', order_id=order_id)
        else:
            return self._request('order_cancel/all', method='post')
