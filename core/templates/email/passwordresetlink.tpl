{% extends "mail_templated/base.tpl" %}

{% block subject %}
بازیابی رمز عبور
{% endblock %}

{% block body %}
برای بازیابی رمز عبور خود به لینک زیر مراجعه کنید:

{{ frontend_url }}/reset-password?token={{ token }}

این لینک تا ۴۸ ساعت معتبر است.

اگر این درخواست را شما نفرستاده‌اید، این ایمیل را نادیده بگیرید.
{% endblock %}

{% block html %}
<!DOCTYPE html>
<html dir="rtl" lang="fa">
<head>
    <meta charset="UTF-8">
</head>

<body style="font-family: Tahoma, Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">

    <div style="max-width: 500px; margin: auto; background: #fff;
                border-radius: 8px; padding: 30px;">

        <h2 style="color: #333;">
            بازیابی رمز عبور
        </h2>

        <p style="color: #555; line-height: 1.8;">
            برای بازیابی رمز عبور خود، روی لینک زیر کلیک کنید.
            این لینک تا ۴۸ ساعت معتبر است.
        </p>

        <div style="text-align: center; margin: 30px 0;">

            <a href="{{ frontend_url }}/reset-password?token={{ token }}"
               style="background-color: #2563eb;
                      color: #fff;
                      padding: 12px 30px;
                      text-decoration: none;
                      border-radius: 6px;
                      display: inline-block;">

                بازیابی رمز عبور

            </a>

        </div>

        <p style="color: #999; font-size: 13px;">
            اگر این درخواست را شما نفرستاده‌اید،
            این ایمیل را نادیده بگیرید.
        </p>

    </div>

</body>
</html>
{% endblock %}