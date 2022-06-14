package causalityprotocols.saturn;

import peersim.core.CommonState;
import peersim.core.Node;
import simulator.protocols.CausalityProtocol;
import simulator.protocols.messages.Message;

public class Saturn extends CausalityProtocol {

	private boolean operationExecuting;
	private String testOperation;

	/**
	 * The constructor for the protocol.
	 */
	public Saturn(String prefix) {
		super(prefix);
	}

	@Override
	public Object clone() {
		Saturn saturn = (Saturn) super.clone();
		saturn.operationExecuting = false;
		return saturn;
	}

	@Override
	public boolean checkCausality(Node node, Message message) {
		if (message.getOperationType() == Message.OperationType.READ) {
			return true;
		}

		//if (message.getOriginNode().getID() == node.getID()) {
		//	return true;
		//}

		System.out.println("Operation Executing - " + message.getMessageId() + " - " + operationExecuting + " - Time: " + CommonState.getTime() + " - Node: - " + CommonState.getNode().getID());

		// If there isn't an operation executing, operation can execute.
		return !operationExecuting;
	}

	@Override
	public void operationFinishedExecution(Node node, Message message) {
		this.operationExecuting = false;
		this.testOperation = null;

		if (message.getOperationType() == Message.OperationType.WRITE) {
			System.out.println("DEBUG - Time:" + CommonState.getTime() + " - Executed - : " + message.getMessageId() + " - Node:" + CommonState.getNode().getID());
			System.out.println();
		}
	}

	@Override
	public void operationStartedExecution(Node node, Message message) {
		this.operationExecuting = true;
		this.testOperation = message.getMessageId();

		/*if (message.getMessageType() == Message.MessageType.WRITE) {
			System.out.println("DEBUG - Time:" + CommonState.getTime() + " - Executing - : " + message.getMessageId() + " - Node:" + CommonState.getNode().getID());
			System.out.println();
		}*/
	}
}
