from pydantic import BaseModel
from typing import List, Optional

# 3-1
class TransactionBase(BaseModel):
    date: str
    category: str
    description: Optional[str]
    amount: int
class CategorySummary(BaseModel):
    category: str
    totalAmount: int
class MonthlySummary(BaseModel):
    month: str
    totalSpent: int
    categories: List[CategorySummary]
    transactions: List[TransactionBase]
class SummaryResponse(BaseModel):
    status: str
    summary: List[MonthlySummary]

    class Config:
        from_attributes = True


# 3-2
class RepaymentStatus(BaseModel):
    totalAmount: int
    paidAmount: int
    remainingAmount: int
class RepaymentChartItem(BaseModel):
    month: str
    paid: int
    interest: float
class RepaymentStatusResponse(BaseModel):
    repaymentStatus: RepaymentStatus
    repaymentChart: List[RepaymentChartItem]

#3-3
# class Category(BaseModel):
#     category_id: int
#     category_name: str
#     saving_percentage: float
# class ConsumptionPlanResponse(BaseModel):
#     selectedPlanName: str
#     total_amount: float
#     duration: int
#     categories: List[Category]
#     hashtags: Optional[List[str]] = None
# class ErrorResponse(BaseModel):
#     status: str
#     message: str