from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from urllib.parse import unquote

from calculatrice_rpn.infra.services.rpn import RPNCalculator


router = APIRouter(prefix="/rpn")
stack_service = RPNCalculator()


@router.get("/op")
def get_op():
    """get all operands"""
    stack = stack_service.get_operands()

    return stack


@router.post("/stack")
def create_stack():
    """create a new stack"""
    stack_id = stack_service.create()
    message = {"id": stack_id}
    return JSONResponse(content=message, status_code=200)


@router.get("/stack/{stack_id}")
def get_stack(stack_id: int):
    """get a stack by it's id

    Args:
        stack_id (int): numeric value
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Raises:
        HTTPException: in case id doesn't exist

    Returns:
        StackResponseSchema: object values
    """
    stack = stack_service.get(stack_id=stack_id)
    if stack is None:
        raise HTTPException(status_code=404, detail="Stack not found")
    return stack


@router.get("/stack")
def get_stacks():
    """List the available stacks"""
    stacks = stack_service.get_stacks()
    if not stacks:
        raise HTTPException(status_code=404, detail="Stacks not found")
    return stacks


@router.post("/stack/{stack_id}")
def push_value(stack_id: int, value: float):
    """Push a new value to a stack"""
    stack = stack_service.push(stack_id=stack_id, value=value)
    if stack is None:
        raise HTTPException(status_code=404, detail="Stack not found")
    return stack


@router.post("/op/{op}/stack/{stack_id}")
def apply_operand(stack_id: int, op: str):
    """Apply an operand to a stack"""
    if op == "%2F":
        op = unquote(op)
    print(op)
    try:
        stack = stack_service.apply_operand(stack_id=stack_id, operand=op)
        if stack is None:
            raise HTTPException(status_code=404, detail="Stack not found")
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except ZeroDivisionError:
        raise HTTPException(status_code=500, detail="Division by zero")
    return stack


@router.delete("/stack/{stack_id}")
def delete_stack(stack_id: int):
    """Push a new value to a stack"""
    stack = stack_service.delete(stack_id=stack_id)
    if stack is None:
        raise HTTPException(status_code=404, detail="Stack not found")
    return stack
