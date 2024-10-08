from typing import Union, List
from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
    await summary.save()
    return summary.id

async def get(id: int) -> Union[dict, None]:
    return await TextSummary.filter(id=id).first()

async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries