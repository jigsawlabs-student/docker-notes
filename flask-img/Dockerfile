# Start base Python image
FROM python
#
# install flask

RUN pip3 install flask

WORKDIR src/

ADD ./app.py ./

WORKDIR ..

#
CMD ["flask"]
# run flask run 
#
#
