/**
 * Copyright (c) 2018-2020 Inria
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are
 * met: redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer;
 * redistributions in binary form must reproduce the above copyright
 * notice, this list of conditions and the following disclaimer in the
 * documentation and/or other materials provided with the distribution;
 * neither the name of the copyright holders nor the names of its
 * contributors may be used to endorse or promote products derived from
 * this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#include "mem/cache/replacement_policies/myown_rp.hh"

#include <cassert>
#include <memory>

// #include "params/FIFORP.hh"
#include "params/MYOWNRP.hh"
#include "sim/cur_tick.hh"

namespace gem5
{

GEM5_DEPRECATED_NAMESPACE(ReplacementPolicy, replacement_policy);
namespace replacement_policy
{

MYOWN::MYOWN(const Params &p)
  : Base(p)
{
}

void
MYOWN::invalidate(const std::shared_ptr<ReplacementData>& replacement_data)
{
    // Reset insertion tick
    std::static_pointer_cast<MYOWNReplData>(
        replacement_data)->tickInserted = Tick(0);
        
    std::static_pointer_cast<MYOWNReplData>(
        replacement_data)->usetimes = 4096;  

      
}

void
MYOWN::touch(const std::shared_ptr<ReplacementData>& replacement_data) const
{
    // A touch does not modify the insertion tick
    std::static_pointer_cast<MYOWNReplData>(
        replacement_data)->tickInserted = curTick();


    std::static_pointer_cast<MYOWNReplData>(
        replacement_data)->usetimes += 1 ;   
}

void
MYOWN::reset(const std::shared_ptr<ReplacementData>& replacement_data) const
{
    // Set insertion tick
    std::static_pointer_cast<MYOWNReplData>(
        replacement_data)->tickInserted = curTick();

    std::static_pointer_cast<MYOWNReplData>(
        replacement_data)->usetimes = 1 ; 
}

ReplaceableEntry*
MYOWN::getVictim(const ReplacementCandidates& candidates) const
{
    // There must be at least one replacement candidate
    //32 times 
    //1024 times


    assert(candidates.size() > 0);

    // Visit all candidates to find victim
    ReplaceableEntry* victim = candidates[0];
    for (const auto& candidate : candidates) {
        // Update victim entry if necessary
        if (std::static_pointer_cast<MYOWNReplData>(
                    candidate->replacementData)->tickInserted <
                std::static_pointer_cast<MYOWNReplData>(
                    victim->replacementData)->tickInserted) {
            victim = candidate;
        }
    }

    //used 32 times
    ReplaceableEntry* victim1 = candidates[0];
    Tick tmp32=288201765000;
    for (const auto& candidate : candidates) {
        // Update victim entry if necessary
        if ((std::static_pointer_cast<MYOWNReplData>(
                    candidate->replacementData)->tickInserted < tmp32)&&
            (std::static_pointer_cast<MYOWNReplData>(
                    candidate->replacementData)->usetimes > 1023 )        
                    ) {
            victim1 = candidate;
            tmp32=std::static_pointer_cast<MYOWNReplData>(
                    victim1->replacementData)->tickInserted;
        }
    } 

    //used 1024 times
    ReplaceableEntry* victim2 = candidates[0];
    Tick tmp1024=400201765000;
    for (const auto& candidate : candidates) {
        // Update victim entry if necessary
        if ((std::static_pointer_cast<MYOWNReplData>(
                    candidate->replacementData)->tickInserted < tmp1024)&&
            (std::static_pointer_cast<MYOWNReplData>(
                    candidate->replacementData)->usetimes > 4095 )        
                    ) {
            victim2 = candidate;
            tmp1024=std::static_pointer_cast<MYOWNReplData>(
                    victim2->replacementData)->tickInserted;
        }
    } 

    if (std::static_pointer_cast<MYOWNReplData>(
                    victim2->replacementData)->usetimes >4095 )
                    {
                        return victim2;
                    }
    else if (std::static_pointer_cast<MYOWNReplData>(
                    victim1->replacementData)->usetimes >1023 )
                    {
                        return victim1;
                    }
    else {
        return victim;
    }

    //return victim;
}

std::shared_ptr<ReplacementData>
MYOWN::instantiateEntry()
{
    return std::shared_ptr<ReplacementData>(new MYOWNReplData());
}

} // namespace replacement_policy
} // namespace gem5
