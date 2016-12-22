from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Homeservices(models.Model):
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    place_id = models.CharField(max_length=1000)
    img = models.CharField(max_length=1000)
    contact = models.CharField(max_length=100, null=True)
    open_now = models.CharField(max_length=1000, null=True, default='True')
    open_time = models.CharField(max_length=1000, null=True, default='1000')
    close_time = models.CharField(max_length=1000, null=True, default='2000')
    rating = models.CharField(max_length=1000, null=True, default='3')
    is_bookmarked = models.BooleanField(default=False)
    type = models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.name


class BookmarkHomeservices(models.Model):
    user = models.ForeignKey(User, default=1)
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    latitude = models.FloatField(null=True,default=1.0)
    longitude = models.FloatField(null=True,default=1.0)
    place_id = models.CharField(max_length=1000)
    img = models.CharField(max_length=1000)
    contact = models.CharField(max_length=100, null=True,default='1')
    open_now = models.CharField(max_length=1000, null=True,default='1000')
    open_time = models.CharField(max_length=1000, null=True,default='1000')
    close_time = models.CharField(max_length=1000, null=True,default='2000')
    rating = models.CharField(max_length=1000, null=True, default='Null')
    type = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name


class Picture(models.Model):
    homeservices_thumb = models.CharField(max_length=1000)
    type = models.CharField(max_length=100)

    def __str__(self):
        return  self.type + ' Pic ' + str(self.pk)

# https://img.buzzfeed.com/buzzfeed-static/static/2015-12/8/3/enhanced/webdr08/enhanced-24614-1449564487-1.jpg
# data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUTExQWFhUVGB0YFRgYGBobGBgfGBgYFxUYFxoYHSggGhooHRcYITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OGhAQGi0lICUtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSstLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLf/AABEIALgBEQMBIgACEQEDEQH/xAAcAAACAgMBAQAAAAAAAAAAAAAFBgMEAAIHAQj/xABDEAABAwIDBQYDBAgFAwUAAAABAgMRACEEEjEFBkFRYRMicYGRoTKxwRRC0eEHI1JicpKi8BUzssLxFiRDU1RjgqP/xAAZAQADAQEBAAAAAAAAAAAAAAABAgMABAX/xAAmEQACAgICAgICAgMAAAAAAAAAAQIRAyESMRNBBFEiMmFxFCOB/9oADAMBAAIRAxEAPwDk+evCqpMFhHHlZW0KWegsPE6CmRvcTElGe08gCoDxULelcspKPbOlJsVwqvQsc6IYzd/EN6tkgcU972F/ahoYVMAGTaIvPhRVMDTRKldbTRnZe5uIdgq7g/mPzgetMjO5jLKc7ykgc3CI9LJ+dTlOKHUWJWCW6FSzmzc0/jp607bGfxShlxCELHMfH5x3flVfE7w4JmyJdI4JEJ9TA9JoPjd93lWbSlodO8r1NvakalP0G0vY0YrYDbhB0M6K+VGWMDgsOyVvF0qE5W20W6SYj3FcdxmOcdMuLUs/vEn05eVFtj73YpjuhXaI/YclXorUetHxSS7BzTDW0N9iiUssBHVy59En6mgR3txmcLD6gRoEwE+kQR4zTKxtbAYsZX0dgs8wC2T4jTziqO1tx1BJWwoLQRYg5h5EXFGPFaaoLt9Ma92P0pplKcT+rVA/WpHcMgTmTcpvPMeFdTwG8zS0gk2IkKT3knqCK4T+k3ZSGnsM622G0v4ZtakpA
# https://lintvksnw.files.wordpress.com/2014/09/ap050712017644.jpg?w=650
# http://ichef-1.bbci.co.uk/news/624/cpsprodpb/F164/production/_90769716_fbc900bf-ab56-447b-b5c2-d9410b8b8d30.jpg
# http://i1.wp.com/corecommunique.com/wp-content/uploads/2014/08/PCG_9685.jpg
# https://s-media-cache-ak0.pinimg.com/564x/54/76/ba/5476bad139aeebb48f99618879c081b7.jpg
# http://www.roomstory.com/media/catalog/product/cache/1/thumbnail/800x600/040ec09b1e35df139433887a97daa66f/d/e/delnew0002_new_punjab_furniture_kirti_nagar_delhi_int8.jpg
# http://hometreo.com/media/wysiwyg/5890_WWI.jpg
# http://timesofindia.indiatimes.com/photo/38092502.cms
# http://www.undolock.com/17/j-fancy-french-country-bedroom-furniture-white-french-country-bedroom-furniture-white-french-country-bedroom-furniture-off-white-french-country-bedroom-furniture-stores-french-country-bedroom-fur-coun-840x630.jpg
