ABOUT
-----
[World Water Day](http://www.waterday.org/) is March 22nd; a day when the world
turns its attention towards the 750 million people who lack access to safe 
water. But every day of the year can be a Water Day. When Rajamma opens her
tap, or Grace hears raindrops filling her catchment system, or when Poppy is
able to offer her children a safe drink of water: each of these is a Water Day.

QUICK INSTALL
-------------
Setup your [virtual environment](http://www.virtualenv.org/)

    $ virtualenv --system-site-packages foobar

Download the [Water Day codebase](https://github.com/waterdotorg/waterday-2015/)

Install local requirements within the virtualenv

    $ pip install -r requirements.txt

Required global packages

    $ apt-get install postgresql python-psycopg2 python-imaging

Setup Postgres Database

    $ su postgres
    $ createuser -P -E foobar
    $ createdb -E UTF8 -T template0 --owner=foobar foobar

Setup Django environment - [Quick install guide](https://docs.djangoproject.com/en/1.6/intro/install/)
    - See comments in settings_default.py file regarding private settings
    
Install Nginx and symlink config file

    $ apt-get install nginx
    $ ln -s /src/foobar/nginx/nginx.conf /etc/nginx/sites-enabled/foobar

Install Supervisor
    - best done outside virtualenv
    - see http://supervisord.org/installing.html

    $ pip install supervisor
    $ sudo echo_supervisord_conf > /etc/supervisord.conf
    $ mkdir /etc/supervisord/
    $ mkdir /var/log/supervisord

See the supervisord/ folder for default daemon scripts and symlink 
to /etc/supervisord/. 

LICENSE
-------
Copyright (C) 2014

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.


CREDITS
-------
A project by [Water.org](http://water.org/). For more than two decades,
Water.org has been at the forefront of developing and delivering solutions to 
the water crisis. Founded by Gary White and Matt Damon, Water.org pioneers 
innovative, community-driven and market-based solutions to ensure all people 
have access to safe water and sanitation; giving women hope, children health 
and communities a future. To date, Water.org has positively transformed the 
lives of more than 1,000,000 individuals living across communities in Africa, 
South Asia, Latin America and the Caribbean; ensuring a better life for 
generations ahead.
