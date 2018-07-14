# -*- coding: utf-8 -*-

# Use this file to easily define all of your cron jobs.
#
# It's helpful to understand cron before proceeding.
# http://en.wikipedia.org/wiki/Cron
#
# Learn more: http://plan.readthedocs.io/

import os

import click
from plan import Job, Plan

path = os.getcwd()
cron = Plan(os.path.basename(path))

# cron.bootstrap('pip install requests')
# cron.bootstrap(['pip install Sphinx', 'sphinx-quickstart'])
# cron.env('MAILTO', 'user@example.com')
# cron = Plan("scripts", path='/web/yourproject/scripts',
#             environment={'YOURAPP_ENV': 'production'})

# job = Job('onejob', every='1.day', at='hour.12 minute.15 minute.45')
# job = Job('job', every='1.day', output=dict(stdout='/tmp/stdout.log', stderr='/tmp/stderr.log'))
# cron.raw('cd /tmp && ruby script.rb > /dev/null 2>&1', every='1.day')

# cron.command(
#     "mysqloptimize xiaoshuo -uxiaoshuo -pdA8aR94mZ5RuesB9",
#     every="sunday",
#     at="hour.4 minute.0",
# )

# cron.command(
#     "mysqlanalyze xiaoshuo -uxiaoshuo -pdA8aR94mZ5RuesB9",
#     every="sunday",
#     at="hour.4 minute.0",
# )

# cron.command(
#     "mysqlcheck xiaoshuo -uxiaoshuo -pdA8aR94mZ5RuesB9",
#     every="sunday",
#     at="hour.4 minute.0",
# )

# cron.command(
#     "/usr/bin/php {}/crontab/interval.php".format(path),
#     every="15.minute",
#     output=dict(
#         stdout="/home/www/logs/interval_stdout.log",
#         stderr="/home/www/logs/interval_stderr.log",
#     ),
# )

# cron.script('script.py', every='1.day', path='/web/yourproject/scripts',
#             environment={'YOURAPP_ENV': 'production'})


@click.command()
@click.argument("action", default="check")
def main(action):
    """
    Available commands:

        check   检查任务脚本变化, 默认设置.\n
        write   写入任务脚本.\n
        clear   清除计划任务.\n
        update  更新任务脚本.
    """
    # click.secho('Hello World!', fg='red')
    # click.echo(click.style('Hello World!', fg='green'))
    cron.run(action)


if __name__ == "__main__":
    main()
