// frontend/app/page.tsx
import PlanPanel from "../components/PlanPanel";
import Gauges from "../components/Gauges";
import Timeline from "../components/Timeline";
import ChatPanel from "./(ui)/chat/ChatPanel";

export default function Page() {
  const base = process.env.NEXT_PUBLIC_API_BASE || "";

  return (
    // grid fills all remaining height from the layout
    <div className="grid h-full grid-cols-1 gap-4 lg:grid-cols-12">
      {/* LEFT: Chat, full-height, internal scroll only */}
      <aside className="lg:col-span-4 h-full overflow-hidden">
        <div className="panel h-full flex flex-col">
          <div className="panel-header">Mission Chat</div>
          <div className="panel-body flex-1 overflow-hidden">
            <ChatPanel />
          </div>
        </div>
      </aside>

      {/* RIGHT: top (gauges+plan) + bottom (timeline) with fixed ratio rows */}
      <section className="lg:col-span-8 h-full overflow-hidden grid grid-rows-[minmax(320px,0.55fr),1fr] gap-4">
        <div className="grid grid-cols-1 gap-4 xl:grid-cols-3 overflow-hidden">
          <div className="xl:col-span-2 overflow-hidden">
            <div className="panel h-full">
              <div className="panel-header">Flight Gauges</div>
              <div className="panel-body h-full overflow-hidden">
                <Gauges backendBase={base} />
              </div>
            </div>
          </div>
          <div className="xl:col-span-1 overflow-hidden">
            <div className="panel h-full">
              <div className="panel-header">ARIA Plan</div>
              <div className="panel-body h-full overflow-hidden">
                <PlanPanel backendBase={base} />
              </div>
            </div>
          </div>
        </div>

        <div className="panel h-full overflow-hidden">
          <div className="panel-header">Timeline</div>
          <div className="panel-body h-full overflow-hidden">
            <Timeline backendBase={base} />
          </div>
        </div>
      </section>
    </div>
  );
}