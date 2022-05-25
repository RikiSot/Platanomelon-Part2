from pydantic import BaseModel, Field


class Iris(BaseModel):
    asymmetry_coefficient: float = Field(..., alias='Asymmetry coefficient')
    Perimeter: float
    length_of_kernel: float = Field(..., alias='Length of kernel')
    Compactness: float
    Area: float
    length_kernel_groove: float = Field(..., alias='Length kernel groove')
    width_of_kernel: float = Field(..., alias='Width of kernel')
