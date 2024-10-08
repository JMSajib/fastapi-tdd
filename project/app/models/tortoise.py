from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator  # new

class TextSummary(models.Model):
    url = fields.TextField()
    summary = fields.TextField()
    create_at = fields.DatetimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.url
    

SummarySchema = pydantic_model_creator(TextSummary)  # new