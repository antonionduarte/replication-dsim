package causality.broadcast;

import causality.messages.Message;
import peersim.core.Node;
import peersim.edsim.EDProtocol;

public interface Broadcast extends EDProtocol {

	/**
	 * Implemented in the {@link BroadcastProtocol} abstract class.
	 * It retrieves the list of neighbors of the current node from the overlay protocol
	 * and calls the uponBroadcast function.
	 * @param node The current node.
	 * @param message The message to broadcast.
	 */
	void broadcastMessage(Node node, Message message);

}
