// frontend/app/page.tsx
import PlanPanel from "../components/PlanPanel";
import Gauges from "../components/Gauges";
import Timeline from "../components/Timeline";
import ChatPanel from "./(ui)/chat/ChatPanel";
import ScenarioControls from "../components/ScenarioControls";

export default function Page() {
  const base = process.env.NEXT_PUBLIC_API_BASE || "";

  return (
    <>
      <div className="mb-3 flex items-center justify-between">
        <div className="text-sm text-muted-foreground">ARIA Mission Control</div>
        <ScenarioControls />
      </div>

      {/* This grid takes all remaining height from <main> */}
      <div className="grid h-full min-h-0 grid-cols-1 gap-4 lg:grid-cols-12">
        {/* LEFT: Chat */}
        <aside className="lg:col-span-4 min-h-0">
          <div className="panel h-full min-h-0 flex flex-col">
            <div className="panel-header">Mission Chat</div>
            <div className="panel-body flex-1 min-h-0">
              <ChatPanel />
            </div>
          </div>
        </aside>

        {/* RIGHT: Gauges+Plan (top) + Timeline (bottom) */}
        <section className="lg:col-span-8 grid min-h-0 grid-rows-[minmax(320px,1fr),1fr] gap-4">
          <div className="grid min-h-0 grid-cols-1 gap-4 xl:grid-cols-3">
            <div className="xl:col-span-2 min-h-0">
              <div className="panel h-full min-h-0 flex flex-col">
                <div className="panel-header">Flight Gauges</div>
                <div className="panel-body flex-1 min-h-0">
                  <Gauges backendBase={base} />
                </div>
              </div>
            </div>
            <div className="xl:col-span-1 min-h-0">
              <div className="panel h-full min-h-0 flex flex-col">
                <div className="panel-header">ARIA Plan</div>
                <div className="panel-body flex-1 min-h-0">
                  <PlanPanel backendBase={base} />
                </div>
              </div>
            </div>
          </div>

          <div className="panel min-h-0 flex flex-col">
            <div className="panel-header">Timeline</div>
            <div className="panel-body flex-1 min-h-0">
              <Timeline backendBase={base} />
            </div>
          </div>
        </section>
      </div>
    </>
  );
}