from django.db import models

# Create your models here.
class Board(models.Model):
    b_no = models.AutoField(db_column='b_no', primary_key=True)
    b_title = models.CharField(db_column='b_title', max_length=255)
    b_note = models.TextField(db_column='b_note', )
    b_writer = models.CharField(db_column='b_writer', max_length=50)
    parent_no = models.IntegerField(db_column='parent_no', default=0)
    b_count = models.IntegerField(db_column='b_count', default=0)
    d_data = models.DateField(db_column='d_data', )
    
    class Meta:
        managed = False
        db_table = 'board'
        
    def __str__(self):
        return "제목 : " + self.b_title + ", 작성자 ; " + self.b_writer
        
    
    
    
    