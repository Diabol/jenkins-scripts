for (agent in hudson.model.Hudson.instance.slaves) { 
    println agent.name + ": " + agent.getComputer().getJnlpMac() 
}
